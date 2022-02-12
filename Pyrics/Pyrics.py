import requests
from lxml import etree
import numpy as np
import time
import pandas as pd
import eng_to_ipa as etipa
import os
from tqdm import tqdm

__version__ = '0.0.1.1' 

class Pyrics:
    
    def __init__(self,path=None):

        if path is None:
            self.path = os.path.join(os.getcwd(), 'lyrics')           
            if not os.path.exists(self.path):
                os.makedirs(os.path.join(self.path, 'rhymes'), exist_ok=True)
                
        else:
            self.path = path
        self.artists = []

        if os.path.exists(os.path.join(self.path, 'rhymes')):
            for data in os.scandir(os.path.join(self.path, 'rhymes')):
                if data.name[-4:] == '.csv':
                    self.artists.append(self.__process_artist_name(data.name[7:-4]))
        
        self.target = 'https://www.azlyrics.com'

        self.__vowel = ['æ', 'ə', 'ɑ', 'ɔ', 'o', 'a', 'e', 'ɛ', 'i', 'ɪ', 'ʊ', 'u', 'ʌ']
        #print(f'Data Path: {self.path}')
        

    def download_lyrics(self, artists, iters_num = 1e20, delay_time=10, fluctuate_rate=5):
        #search
        target = self.target
        artist_search = artists
        search_url = requests.get(f"https://search.azlyrics.com/search.php?q={artist_search.replace(' ', '+')}")
        search_content = etree.HTML(search_url.content)
        artist_url = search_content.xpath('//b[contains(string(), "Artist results:")]/../..//a/@href')[0]
        artist = self.__find_artist(artists, search_content)
        if artist is None:
            return
        
        tree = etree.HTML(requests.get(artist_url).content)
        #album_names = tree.xpath('//div[@class="album"]/b/text()')
        song_names = tree.xpath('//div[@class="listalbum-item"]/a/text()')
        song_urls = tree.xpath('//div[@class="listalbum-item"]/a/@href')
        for content in zip(song_names[0:5], song_urls[0:5]):
            print(f'example songs: {content[0]}: {target + content[1]}')
        
        #download songs
        lyrics_dict = dict()
        lyrics = np.array([])
        songs = np.array([])
        bands = []
        
        #delay_time = 10 # delay time to get rid of being baned
        total_iters = np.min((iters_num, len(song_urls)))
        iters = 1
        with tqdm(total=total_iters) as pbar:
                for content in zip(song_names, song_urls):
                    
                    song_name = content[0]
                    url = content[1]
                    fluctuate = np.abs(np.random.randn())* fluctuate_rate

                    url = requests.get(target + url)
                    tree = etree.HTML(url.content)
                    lyric = np.array([l.strip() for l in tree.xpath('//div[5]/text()') if l.strip()!=''])
                    lyrics = np.hstack([lyrics, lyric])
                    songs = np.hstack([songs, np.array([song_name for i in range(len(lyric))])])
                    #comment = [c.strip() for c in tree.xpath('//div[@class="panel album-panel noprint"]/text()') if c.strip()!='']
                    #print(song_name)
                    pbar.set_description_str(f'{song_name}: delay time: {delay_time + fluctuate} ')
                    if len(lyric) == 0:
                        print('You may be banned')
                        break
                    pbar.update(1)
                    iters += 1
                    if (iters > iters_num or iters == len(song_urls)):
                        break
                    #print(f'delay: {delay_time + fluctuate}')
                    time.sleep(delay_time + fluctuate)
            
        #save file
        bands = [artist for i in range(len(lyrics))]
        lyrics = lyrics.tolist()
        lyrics_dict = {'bands': bands, 'songs': songs, 'lyrics': lyrics}
        df = pd.DataFrame(lyrics_dict)
        print(df)
        df.to_csv(os.path.join(self.path, f'{self.__process_artist_name(artist)}.csv'), index=False)
    
    def __find_artist(self, artist_search, content=None):
        #search
        if content is not None:
            search_tree = content
        else:
            search_url = requests.get(f"https://search.azlyrics.com/search.php?q={artist_search.replace(' ', '+')}")
            search_tree = etree.HTML(search_url.content)
        
        artist = search_tree.xpath('//b[contains(string(), "Artist results:")]/../..//a/span/b/text()')[0]
        if_continue = input(f'Is "{artist}" you search for? (type anything to cancel)\n')
        if if_continue:
            print('Canceled')
            return
        return artist

    def get_rhymes(self, str1):
        
        ipa = etipa.convert(str1, keep_punct=False, stress_marks=None)
        result = []
        iters = 0
        tolerate_flag = False 
        while True:
            iters += 1
            if iters > len(ipa):
                break
                
            if ipa[-iters] not in self.__vowel:
                if not tolerate_flag:
                    result.append(ipa[-iters])
                else:
                    break
            else:
                result.append(ipa[-iters])
                if not tolerate_flag:
                    tolerate_flag = True
                    continue
                
        return ''.join(result[: : -1])

    def generate_rhymes(self, artist_search):
        # find artist
        artist = self.__find_artist(artist_search)
        if artist is None:
            return
        
        # read file
        df_data = self.__read_csv(artist)

        rhymes = []
        lyrics = []
        rhymes_dict = dict()

        total_iters = len(df_data['lyrics'])
        # generate rhyme
        with tqdm(total=total_iters) as pbar:
            for lyric in df_data['lyrics']:
                rhyme = self.get_rhymes(lyric.split()[-1])
                rhymes.append(rhyme)
                lyrics.append(lyric)
                pbar.update(1)
        rhymes_dict.update({ 'rhymes': rhymes})
        
        #save file
        df_rhyme = pd.DataFrame(rhymes_dict)
        df_out = pd.concat([df_data, df_rhyme], axis=1)
        if not os.path.exists(os.path.join(self.path, 'rhymes')):
            os.makedirs(os.path.join(self.path, 'rhymes'), exist_ok=True)
        df_out.to_csv(os.path.join(self.path, 'rhymes', f'rhymes_{self.__process_artist_name(artist)}.csv'), index=False,encoding='utf_8_sig')
        print(df_out)

    def get_rhymes_lyrics(self, lyrics, artists, length=10, exclude=True, same=False, print_lyrics=False):
        data = pd.DataFrame()
        if isinstance(artists,str):
            data = data.append(self.__read_csv(artists, True))
        else:
            for artist in artists: 
                data = data.append(self.__read_csv(artist, True))
        
        # find vowel
        rhymes = self.get_rhymes(lyrics)
        if same:
            match_lyrics = data[data.rhymes == rhymes]
        else:
            rhymes_list = []
            for i in range(len(rhymes)):
                if rhymes[i] in self.__vowel:
                    rhymes_list.append(rhymes[i])
                else:
                    break    
                
        match_lyrics = data[data['rhymes'].str[0: len(rhymes_list)] == ''.join(rhymes_list)]
        
        if exclude:
            match_lyrics = match_lyrics[lyrics.split()[-1] != match_lyrics['lyrics']
                                    .str.translate(str.maketrans(dict.fromkeys('!?.)";', '')))
                                    .str.split().str[-1]]
            
        match_lyrics.reset_index(drop=True, inplace=True)
        output_size = match_lyrics.shape[0]
        indice = np.random.randint(low=output_size, size=np.min((output_size, length)))
    
        match_lyrics = match_lyrics.loc[indice]
        match_lyrics.reset_index(drop=True, inplace=True)
        if print_lyrics:
            for i in range(len(match_lyrics)):
                print(f"{i+1}.{match_lyrics.loc[i]['lyrics']} - {match_lyrics.loc[i]['bands']} <{match_lyrics.loc[i]['songs']}>", end='\n')
        return match_lyrics

    def get_relevant_lyrics(self, lyrics, artists, length=10):
        data = pd.DataFrame()
        if isinstance(artists,str):
            data = data.append(self.__read_csv(artists, True))
        else:
            for artist in artists: 
                data = data.append(self.__read_csv(artist, True))

        match_lyrics = data[data['lyrics'].str.contains(lyrics)]
            
        match_lyrics.reset_index(drop=True, inplace=True)
        output_size = match_lyrics.shape[0]
        indice = np.random.randint(low=output_size, size=np.min((output_size, length)))
        
        return match_lyrics.loc[indice]

    def generate_lyrics(self, inputs, artists, paragraph_length=4, lyrics_length=16, relevant=True, same=False, print_lyrics=False ):

        results = np.array([])
        relevants = []
        if relevant:
            relevants.append([l for l in self.get_relevant_lyrics(inputs, artists, lyrics_length // paragraph_length)['lyrics']])
            for i in range(lyrics_length // paragraph_length):    
                inputs = relevants[0][i]
                results = np.hstack((results, inputs, [l for l in self.get_rhymes_lyrics(inputs, artists, paragraph_length -1, same=same)['lyrics']]))
        else:
            for i in range(lyrics_length // paragraph_length):
                results = np.hstack((results, [l for l in self.get_rhymes_lyrics(inputs, artists, paragraph_length, same=same)['lyrics']]))
                inputs = results[i][0].split()[0]

        results = np.array(results).reshape(-1,1)
        
        if print_lyrics:
            for i in range(len(results)):
                print(results[i][0])
                if (i+1) % paragraph_length == 0:
                    print('\n')
                
        return results
    def get_artists(self):
        return self.artists
    
    def __process_artist_name(self, artist):
            return artist.replace('/','／') .replace('\\','＼')

    def __read_csv(self, artist, rhymes=False):
        # read file
        if rhymes:
            return pd.read_csv(os.path.join(self.path, 'rhymes', f'rhymes_{self.__process_artist_name(artist)}.csv'))
        else:
            return pd.read_csv(os.path.join(self.path, f'{self.__process_artist_name(artist)}.csv'))

# if __name__ == '__main__':
#     band = 'motley crue'
#     pyrics = Pyrics()
#     pyrics.download_lyrics(band, 2)
#     pyrics.generate_rhyme(band)
