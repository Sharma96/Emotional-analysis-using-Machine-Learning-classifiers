import pickle
from nltk.tokenize import word_tokenize as w

emotions = ['anger','anticipation','disgust','fear','joy','sad','surprise','trust']

def negation(tweet):
    keywords={"don't","never","nothing","nowhere","noone","none","not","hasn't","hadn't","can't","couldn't","shouldn't","won't","wouldn't","don't","doesn't","didn't","isn't","aren't","ain't"}
    neg_count = []
    for i in range(len(tweet)):
        neg_count.append(0)
    for neg in keywords:
        if neg in tweet:
            for i in range(len(tweet)):
                if i >= tweet.index(neg):
                    neg_count[i] = neg_count[i] + 1
    for i in range(len(tweet)):
        if neg_count[i] % 2 == 1:
            tweet[i] = "NEG_" + tweet[i]
    return tweet

# Creating feature vectors for the latest user tweets
def createTestSet(userName):

    print('Creating test vector set')

    file = open('SVM/UserData/%s_latest_tweets' %userName, 'rb')
    tweets = pickle.load(file)

    data = []

    for i in range(0,len(tweets)):
        tweet = tweets[i]
        tweet = tweet.lower()
        text = w(tweet)
        text = negation(text)

        vector = [0, 0, 0, 0, 0, 0, 0, 0]
        index = -1

        for emotion in emotions:
            file = open('SVM/EmotionLexicons/%s.txt' % emotion, 'r')
            vocab = file.read().split()

            index += 1

            for word in text:
                if word in vocab:
                    vector[index] += 1

        data.append(vector)

    file = open('SVM/UserData/%s_test_vectors' % userName, 'wb')
    pickle.dump(data, file)
    print('Created test vector set\n')

