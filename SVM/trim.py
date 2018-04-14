from bs4 import BeautifulSoup
import re
import itertools
from nltk.tokenize import word_tokenize as w


def preprocessTweets(tweet):

    # 1 Remove HTML Tags
    soup = BeautifulSoup(tweet, 'html.parser')
    cleaned_tweet = soup.get_text()

    # 2 Remove appostrophes
    appostrophes= {"'s" : " is", "'re": " are", "n't" : "not", "'d" : " had" , "'m":" am", "'ve":" have", "lol" : "laugh out loud", "luv" : "love"}

    slist = w(cleaned_tweet)
    newsen=[]

    for word in slist:
        for candid in appostrophes:
            if candid in word:
                word=word.replace(candid,appostrophes[candid])
        newsen.append(word)

    cleaned_tweet=" ".join(newsen)

    # 3 Split attached words
    ans = ""
    for a in re.findall('[A-Z][^A-Z]*',cleaned_tweet):
        ans += a.strip()+' '
    cleaned_tweet = ans

    # 4 Standardizing words like i am happpppyyy to i am happy
    temp =''.join(''.join(s)[:2] for _, s in itertools.groupby(cleaned_tweet))
    cleaned_tweet = temp

    # 5 Remove URL
    cleaned_tweet= re.sub(r"http\S+.*", " ",cleaned_tweet)
    cleaned_tweet = re.sub(r"http.*", " ", cleaned_tweet)

    # 6 Slang Lookup

    # sentence_list = w(cleaned_tweet)
    #
    # # make a place where we can build our new sentence
    # new_sentence = []

    # # look through each word
    # for word in sentence_list:
    #     # look for each candidate
    #     for candidate_replacement in appostrophes:
    #         # if our candidate is there in the word
    #         if candidate_replacement in word:
    #             # replace it
    #             word = word.replace(candidate_replacement, appostrophes[candidate_replacement])
    #
    #     # and pop it onto a new list
    #     new_sentence.append(word)
    #
    # cleaned_tweet = " ".join(new_sentence)

    return cleaned_tweet