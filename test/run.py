import sys
import os

from soupsieve import match
 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parentdir)

from Pyrics import Pyrics as p

g_changed_artist = set()

def mode(inputs):
    try:
         return int(inputs)
    except Exception as e:
        print(e)
    

def main(mode_number, artists):
    try:
        if mode_number == 1:

            while(True):
                theme = input('input theme: \n')
                print('')
                prc.generate_lyrics(theme, artists,  relevant=True, print_lyrics=True)
                
        elif mode_number == 2:

            while(True):
                inputs = input('input keywords: \n')
                if(inputs == ''):
                    raise ValueError('please input')
                print('')

                prc.get_relevant_lyrics(inputs, artists, print_lyrics=True)
        

        elif mode_number == 3:

            while(True):
                inputs = input('input lyrics: \n')
                print('')
                prc.get_rhymes_lyrics(inputs, artists, print_lyrics=True)

        elif mode_number == 4:
            
            inputs = input('input artists you want to download\n')
            number = int(input('how many songs to download? <0 means all>\n'))
            if number < 0:
                raise ValueError('not positive integer')
            elif number == 0:
                number = 1e20
            prc.download_lyrics(artists=inputs, iters_num=number)
                
        elif mode_number == 5:
            
            inputs = input('input artists you want to generate rhymes\n')
            prc.generate_rhymes(inputs)

        elif mode_number == 6:
            g_changed_artist.clear()
            artist = prc.get_artists()
            for i in range(len(artist)):
                print(f'{i+1}.{artist[i]}')
            inputs = input('choose the artists <0 means all/ split with space>\n')
            inputs = inputs.split(' ')

            for number in inputs:
                if int(number) < 0 or int(number) > len(artist):
                    raise ValueError('input correct value')

            if '0' in inputs:
                artists = prc.get_artists()
            else:
                for index in [int(idx) for idx in inputs]:
                    g_changed_artist.add(artist[index-1])
                print(g_changed_artist)
            
        elif mode_number == 7:
            for artist in artists:
                print(artist)

        elif mode_number == 8:
                print(prc.path)   

    except FileExistsError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f'sorry, we cannot write about this ({e})')

if __name__ == '__main__':
    artists_list = []
    while True:
        prc = p.Pyrics()

        if len(g_changed_artist) == 0:
            artists_list = prc.get_artists()
        else:
            artists_list = [artist for artist in g_changed_artist]
        
        mode_number = mode(input('\n\
                                choose mode: \n\
                            1.generate theme lyrics \n\
                            2.get relevant lyrics \n\
                            3.get rhyme lyrics \n\
                            4.download lyrics \n\
                            5.generate rhymes \n\
                            6.change artists \n\
                            7.see data artists\n\
                            8.see data path\n\
                            <1-8>\n'))
        if mode_number not in range(1,9):
            print('please choose correct mode')
            continue
        main(mode_number, artists_list)


    

