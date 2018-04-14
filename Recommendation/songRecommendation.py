import requests
import xml.etree.ElementTree as ET
import os

def recommendation(param_emotion):

    song_genre_1 = {'anger': 'calm',
                    'anticipation': 'cool',
                    'disgust': 'soul',
                    'fear': 'electro',
                    'enjoyment': 'disco',
                    'sad': 'happy',
                    'surprise': 'pop',
                    'trust': 'trance'}

    song_genre_2 = {'anger': 'jazz',
                    'anticipation': 'dubstep',
                    'disgust': 'rock',
                    'fear': 'reggae',
                    'enjoyment': 'funk',
                    'sad': 'happy',
                    'surprise': 'techno',
                    'trust': 'folk'}

    mood = param_emotion

    params1 = {'fct': 'getfromtag', 'tag': song_genre_1[mood], 'apikey': 'o7zw93v1'}
    params2 = {'fct': 'getfromtag', 'tag': song_genre_2[mood], 'apikey': 'o7zw93v1'}

    link = 'http://musicovery.com/api/V4/playlist.php'

    res1 = requests.get(link, params=params1)
    res2 = requests.get(link, params=params2)

    filename = mood + '-' + song_genre_1[mood]
    file1 = open('Recommendation/playlist/%s_songs.txt' % filename, 'w')

    filename = mood + '-' + song_genre_2[mood]
    file2 = open('Recommendation/playlist/%s_songs.txt' % filename, 'w')

    file1.write(res1.text)
    file2.write(res2.text)

    # Removing garbage value
    filename = mood + '-' + song_genre_1[mood]
    with open('Recommendation/playlist/%s_songs.txt' % filename, 'r') as fin:
        data = fin.read().splitlines(True)
    with open('Recommendation/playlist/%s_songs.xml' % filename, 'w') as fout:
        fout.writelines(data[2:])

    filename = mood + '-' + song_genre_2[mood]
    with open('Recommendation/playlist/%s_songs.txt' % filename, 'r') as fin:
        data = fin.read().splitlines(True)
    with open('Recommendation/playlist/%s_songs.xml' % filename, 'w') as fout:
        fout.writelines(data[2:])

    # deleting redundant text files
    filename = mood + '-' + song_genre_1[mood]
    os.remove('Recommendation/playlist/%s_songs.txt' % filename)
    filename = mood + '-' + song_genre_2[mood]
    os.remove('Recommendation/playlist/%s_songs.txt' % filename)

    # Parsing XML
    filename = mood + '-' + song_genre_1[mood]
    tree1 = ET.parse('Recommendation/playlist/%s_songs.xml' % filename)
    filename = mood + '-' + song_genre_2[mood]
    tree2 = ET.parse('Recommendation/playlist/%s_songs.xml' % filename)

    root1 = tree1.getroot()
    root2 = tree2.getroot()

    tracks1 = root1.find('tracks').findall('track')
    tracks2 = root2.find('tracks').findall('track')

    limit = 0
    songlist = []

    for t in tracks1:

        songname = t.find('title').text
        artistname = t.find('artist').find('name').text
        temp = songname + "-" + artistname
        songlist.append(temp)

        limit += 1
        if limit == 1:
            break

    limit = 0

    for t in tracks2:

        songname = t.find('title').text
        artistname = t.find('artist').find('name').text
        temp = songname + "-" + artistname
        songlist.append(temp)

        limit += 1
        if limit == 1:
            break

    songlist = list(set(songlist))
    return songlist
