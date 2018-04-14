from bs4 import BeautifulSoup as SOUP
import re
import requests as http


def recommendation(emotion):

    movies = []

    qw = {'sad': 'comedy.txt', 'disgust': 'romance.txt', 'anger': 'fantasy.txt', 'anticipation': 'mystery.txt',
          'fear': 'animation.txt', 'enjoyment': 'western.txt', 'trust': 'music.txt', 'surprise': 'horror.txt'}
    for k, v in qw.items():

        if k == emotion:
            i = 0
            v = 'Recommendation/movies/' + v
            for line in open(v, 'r').readlines():
                movies.append(line)
                if i > 2:
                    break

                i += 1

    if emotion == "sad":
        urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter,asc'

    elif emotion == "disgust":
        urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter,asc'

    elif emotion == "anger":
        urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter,asc'

    elif emotion == "anticipation":
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter,asc'

    elif emotion == "fear":
        urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter,asc'

    elif emotion == "enjoyment":
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter,asc'

    elif emotion == "trust":
        urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter,asc'

    elif emotion == "surprise":
        urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter,asc'

    response = http.get(urlhere)

    data = response.text
    soup = SOUP(data, "lxml")
    title = soup.find_all("a", attrs={"href": re.compile(r'\/title\/tt+\d*\/')})

    a = title
    count = 0

    if emotion == "disgust" or emotion == "anger" or emotion == "surprise":

        for i in a:
            tmp = str(i).split('>')
            if len(tmp) == 3:
                movies.append(tmp[1][:-3])
            if count > 2:
                break
            count += 1
    else:

        for i in a:
            tmp = str(i).split('>')
            if len(tmp) == 3:
                movies.append(tmp[1][:-3])
            if count > 2:
                break
            count += 1

    return movies
