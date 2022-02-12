## Pyrics
<font size =5>**Pyrics** is a tool to scrape lyrics, get rhymes, **generate** relevant lyrics with **rhymes**.
<font>

### Installation
```python
pip install Pyrics
```

### 	Initilization
```python
from Pyrics import Pyrics as prc

prc = prc.Pyrics()
#prc = prc.Pyrics(path)
```
### Generate Datasets 
```python
artists = 'Led Zeppelin'
```
#### 1.Download Lyrics
```python
#default iters_num = 1e20
download_lyrics(artists=artists, iters_num = 5, delay_time=10, fluctuate_rate=5):
```

|    | bands        | songs                     | lyrics                                                                          |
|---:|:-------------|:--------------------------|:--------------------------------------------------------------------------------|
|  0 | Led Zeppelin | Good Times Bad Times      | In the days of my youth, I was told what it means to be a man                   |
|  1 | Led Zeppelin | Good Times Bad Times      | And now I've reached that age, I've tried to do all those things the best I can |
|  2 | Led Zeppelin | Good Times Bad Times      | No matter how I try, I find my way into the same old jam                        |
|  3 | Led Zeppelin | Good Times Bad Times      | Good times, bad times, you know I've had my share                               |
|  4 | Led Zeppelin | Good Times Bad Times      | When my woman left home with a brown eyed man                                   |
|  5 | Led Zeppelin | Good Times Bad Times      | But I still don't seem to care         

#### 2.Generate Lyrics Data with Rhymes
```python
generate_rhymes(artist_search=artists)
```

|      | bands        | songs                                   | lyrics                                                                               | rhymes   |
|-----:|:-------------|:----------------------------------------|:-------------------------------------------------------------------------------------|:---------|
|    0 | Led Zeppelin | Good Times Bad Times                    | In the days of my youth, I was told what it means to be a man                        | ?n       |
|    1 | Led Zeppelin | Good Times Bad Times                    | And now I've reached that age, I've tried to do all those things the best I can      | ?n       |
|    2 | Led Zeppelin | Good Times Bad Times                    | No matter how I try, I find my way into the same old jam                             | ?m       |
|    3 | Led Zeppelin | Good Times Bad Times                    | Good times, bad times, you know I've had my share                                    | ?r       |
|    4 | Led Zeppelin | Good Times Bad Times                    | When my woman left home with a brown eyed man                                        | ?n       |
|    5 | Led Zeppelin | Good Times Bad Times                    | But I still don't seem to care                                                       | ?r       |


### Core Function: Generate Songs Lyrics
**Combine** the lyrics randomly to **generate** songs with **rhymes**
```python
keyword = 'baby'
artists = ['Guns N\' Roses', 'the doors','led zeppelin']
```
#### 1.Generate Songs Lyrics about Keywords with Rhymes
```python
generate_lyrics(inputs=keyword, artists=artists, paragraph_length=4, lyrics_length=16, relevant=True, same=False, print_lyrics=True )
```
```markdown
I gotta tell you baby
Save our city
Think of me as just a dream
Changes fill my time, baby, that's alright with me


Tell me, baby, what's my name
Alright, okay, alright, okay!
All that amounts to is love that you fed by perversion and pain
In fact, they look so strange


Tell you, pretty baby
Changes fill my time, baby, that's alright with me
I'm from South Philadelphia
It'd be enough, but just my luck, I fell in love and maybe


When the levee breaks, baby you've got to move, you got to move now
I see you walking around
People talking all around
Break it down
```
#### 2.Generate Song Lyrics with the Same Rhymes of Input
```python
generate_lyrics(inputs=keyword, artists=artists, paragraph_length=4, lyrics_length=16, relevant=False, same=False, print_lyrics=True )
```
```markdown
She just puts around, being lazy
Somebody, somebody
Oh baby, baby, I like your honey and it sure likes me
If I could teach my hands to see


Noon burned gold into our hair
Gonna love you, baby, here I come again
Lost cells
But now, could you blow it all on a million-dollar bet


I never wanted you to be someone afraid to know themselves
And now I can't get back again
Please, Mr. Fireman, won't you ring your bell?
Craze, baby, the rainbow's end


Down in the pits you go no lower
You don't have to go, oh, oh, oh, oh
To a strange night of stone
Oh yeah, oh yeah, oh, oh, oh
```

### Basic Function

```python
lyrics = 'Don\'t you cry tonight'
artists = ['Guns N\' Roses', 'the doors','led zeppelin']
```
#### 1.Get Rhymes of Lyrics
```python
get_rhymes(lyrics)

=>'a?t'
```
#### 2.Get the Lyrics with the Same Rhymes
```python
get_rhymes_lyrics(lyrics=lyrics, artists, length=5, exclude=True, same=False, print_lyrics=False):
```

|    | bands         | songs                                | lyrics                                                   | rhymes   |
|---:|:--------------|:-------------------------------------|:---------------------------------------------------------|:---------|
|  0 | Led Zeppelin  | Heartbreaker                         | Abuse my love a thousand times                           | a?mz     |
|  1 | The Doors     | Peace Frog                           | (She came) The women are crying                          | a???     |
|  2 | Guns N' Roses | Oh My God                            | Well, this is better than a good compromise              | a?z      |
|  3 | Guns N' Roses | Don't Cry                            | Talk to me softly, there's something in your eyes        | a?z      |
|  4 | The Doors     | Someday Soon                         | But you're going to die                                  | a?       |
|  5 | The Doors     | Break On Through (To The Other Side) | She get high                                             | a?       |


#### 3.Get Relevant Lyrics about Input Lyrics
```python
get_relevant_lyrics(lyrics=lyrics, artists=lyrics, length=5):
```

|    | bands         | songs                        | lyrics                                                                                             | rhymes   |
|---:|:--------------|:-----------------------------|:---------------------------------------------------------------------------------------------------|:---------|
| 42 | Guns N' Roses | Don't Cry (Alternate Lyrics) | Don't you cry tonight, baby, maybe someday                                                         | e?       |
| 58 | The Doors     | Good Rockin'                 | Well I heard the news, there's good rockin' tonight                                                | a?t      |
| 25 | Guns N' Roses | Don't Cry                    | And don't you cry tonight                                                                          | a?t      |
| 69 | Led Zeppelin  | Fool In The Rain             | Why can't I see you tonight?                                                                       | a?t      |
| 65 | Led Zeppelin  | The Battle Of Evermore       | The dark Lord rides in force tonight                                                               | a?t      |


