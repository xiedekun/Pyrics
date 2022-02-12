# Pyrics
<font size =5>**Pyrics** is a tool to scrape lyrics, get rhymes, **generate** relevant lyrics with **rhymes**.

./test/run.py provides the full function in terminal
```python
cmd>> python run.py
```
or
```python
cmd>> conda activate
conda>> python run.py
```
Author: DK Xie
<font>

## Installation
```python
pip install Pyrics
```

## Initialization
#### Way 1: Not Exist Data
```python
from Pyrics import Pyrics as prc

prc = prc.Pyrics()
```

#### Way 2: Already Exist Data
```python
from Pyrics import Pyrics as prc

prc = prc.Pyrics(path)
```
if exist data folder 'lyrics', folder strucure:
```markdown
-lyrics
   -rhymes
 ```
lyric data (.csv) in lyrics folder, e.g.,
|    | bands          | songs          | lyrics                                            |
|---:|:---------------|:---------------|:--------------------------------------------------|
|  0 | Little Richard | Tutti Frutti   | Wop-bop-a-loo-mop alop-bom-bom                    |
|  1 | Little Richard | Tutti Frutti   | Tutti frutti, oh rutti                            |
|  2 | Little Richard | Tutti Frutti   | Tutti frutti, woo!                                |
|  3 | Little Richard | Tutti Frutti   | Tutti frutti, oh rutti                            |
|  4 | Little Richard | Tutti Frutti   | Tutti frutti, oh rutti                            |
|  5 | Little Richard | Tutti Frutti   | Tutti frutti, oh rutti                            

rhyme data (.csv) in rhymes folder, e.g.,
|    | bands          | songs          | lyrics                                            | rhymes   |
|---:|:---------------|:---------------|:--------------------------------------------------|:---------|
|  0 | Little Richard | Tutti Frutti   | Wop-bop-a-loo-mop alop-bom-bom                    | om       |
|  1 | Little Richard | Tutti Frutti   | Tutti frutti, oh rutti                            | i        |
|  2 | Little Richard | Tutti Frutti   | Tutti frutti, woo!                                | u        |
|  3 | Little Richard | Tutti Frutti   | Tutti frutti, oh rutti                            | i        |
|  4 | Little Richard | Tutti Frutti   | Tutti frutti, oh rutti                            | i        |
|  5 | Little Richard | Tutti Frutti   | Tutti frutti, oh rutti                            | i        |

## Generate Datasets 
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


## Basic Function

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
get_rhymes_lyrics(lyrics=lyrics, artists=artists, length=5, exclude=True, same=False, print_lyrics=False):
```

|    | bands         | songs                                | lyrics                                                   | rhymes   |
|---:|:--------------|:-------------------------------------|:---------------------------------------------------------|:---------|
|  0 | Led Zeppelin  | Heartbreaker                         | Abuse my love a thousand times                           | a?mz     |
|  1 | The Doors     | Peace Frog                           | (She came) The women are crying                          | a???     |
|  2 | Guns N' Roses | Oh My God                            | Well, this is better than a good compromise              | a?z      |
|  3 | Guns N' Roses | Don't Cry                            | Talk to me softly, there's something in your eyes        | a?z      |
|  4 | The Doors     | Someday Soon                         | But you're going to die                                  | a?       |
|  5 | The Doors     | Break On Through (To The Other Side) | She get high                                             | a?       |


#### 3.Get Relevant Lyrics contain Input Lyrics
```python
lyrics = 'I love you'
get_relevant_lyrics(lyrics=lyrics, artists=artists, length=5):
```

|    | bands         | songs             | lyrics                                                                     | rhymes   |
|---:|:--------------|:------------------|:---------------------------------------------------------------------------|:---------|
| 18 | The Doors     | Ships w/Sails     | Well, you asked how much I love you                                        | u        |
| 32 | Led Zeppelin  | Darlene           | And I love you, Yes I do                                                   | u        |
| 31 | Led Zeppelin  | Darlene           | Cause I love you, Darlene                                                  | in       |
| 12 | The Doors     | Hello, I Love You | Hello, I love you                                                          | u        |
|  3 | Guns N' Roses | Prostitute        | Where would you go if I told you I love you and then walked away? Oh, yeah | ?        |
int(None)



## Core Function: Generate Songs Lyrics
**Combine** the lyrics randomly to **generate** songs with **rhymes**
```python
keyword = 'baby'
artists = ['Guns N\' Roses', 'the doors','led zeppelin']
```
#### 1.Generate Songs Lyrics contain Keywords with Rhymes
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
