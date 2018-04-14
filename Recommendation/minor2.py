import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
import pickle as pp
import numpy as np

i = 1;
ter = None;


class abc:
    def __init__(self):
        self.i = 0
        self.A = []
        self.row = 0
        self.col = 0
        self.te = "";

    def fetchInfo(abc, url):
        body = requests.get(url)
        soup = BeautifulSoup(body.text)
        # page = urllib2.urlopen(url).read()
        # soup = BeautifulSoup(page)
        # counter1 = counter1 + 1
        # nextUrl = soup.find('a',attrs={'href':re.compile("ref_=gnr_mn_ac_mp")})
        ans = soup.find_all('a', attrs={'href': re.compile(r"/title/.*adv_li_tt")});
        print(ans);
        for i in ans:
            tmp = str(i).split('>')
            if (len(tmp) == 3):
                # print(tmp[1][:-3])
                qww = tmp[1][:-3]
                abc.te = "%s\n%s" % (abc.te, qww);
        abc.i = abc.i + 1;
        if abc.i == 4:
            return abc.te
        abc.i = 1;
        # print(abc.te);
        global ter;
        ter = "";
        print(abc.te);
        ter = abc.te;
        abc.te = ""
        return ter;


# class final():

def fin():
    za = abc()
    myfile = open('comedy.txt', 'w')
    wr = csv.writer(myfile, dialect='excel')
    te = za.fetchInfo("http://www.imdb.com/search/title?genres=comedy&title_type=feature&sort=moviemeter,asc")
    myfile.write(te);
    myfile.close();
    myfile = open('comedy.txt', 'r')
    myfile.close();

    myfile1 = open('western.txt', 'w')
    wr = csv.writer(myfile1, dialect='excel')
    te5 = za.fetchInfo("http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter,asc")
    myfile1.write(te5);
    myfile1.close();

    myfile = open('romance.txt', 'w')
    wr = csv.writer(myfile, dialect='excel')
    te1 = za.fetchInfo("http://www.imdb.com/search/title?genres=romance&title_type=feature&sort=moviemeter,asc")
    myfile.write(te1);
    myfile.close();

    myfile = open('mystry.txt', 'w')
    wr = csv.writer(myfile, dialect='excel')
    te3 = za.fetchInfo("http://www.imdb.com/search/title?genres=mystry&title_type=feature&sort=moviemeter,asc")
    myfile.write(te3);
    myfile.close();

    myfile = open('fantasy.txt', 'w')
    wr = csv.writer(myfile, dialect='excel')
    te2 = za.fetchInfo("http://www.imdb.com/search/title?genres=fantasy&title_type=feature&sort=moviemeter,asc")
    myfile.write(te2);
    myfile.close();

    myfile = open('animation.txt', 'w')
    wr = csv.writer(myfile, dialect='excel')
    te4 = za.fetchInfo("http://www.imdb.com/search/title?genres=animation&title_type=feature&sort=moviemeter,asc")
    myfile.write(te4);
    myfile.close();

    myfile = open('music.txt', 'w')
    wr = csv.writer(myfile, dialect='excel')
    te6 = za.fetchInfo("http://www.imdb.com/search/title?genres=music&title_type=feature&sort=moviemeter,asc")
    myfile.write(te6);
    myfile.close();

    myfile = open('horror.txt', 'w')
    wr = csv.writer(myfile, dialect='excel')
    te7 = za.fetchInfo("http://www.imdb.com/search/title?genres=horror&title_type=feature&sort=moviemeter,asc")
    myfile.write(te7);
    myfile.close();