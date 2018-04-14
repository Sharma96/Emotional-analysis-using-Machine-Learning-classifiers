import pickle
from nltk.tokenize import word_tokenize as w

emotions = ['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sad', 'surprise', 'trust']

# file = pd.read_csv('new_dataset.csv')
# tweets = file.values.tolist()
#
# with open('./training_tweets','wb') as f:
#     pickle.dump(tweets,f)
#     f.close()

# Loading training tweets
f = open('SVM/training_tweets', 'rb')
tweets = pickle.load(f)
f.close()

data = []

# Looping over each word in each tweet to produce an 8 dimensional feature vector
for i in range(0, len(tweets)):
    raw_tweet = tweets[i][1]
    raw_tweet = w(raw_tweet.lower())

    vector = [0,0,0,0,0,0,0,0]
    index = -1

    for emotion in emotions:
        file = open('SVM/EmotionLexicons/%s.txt' % emotion, 'r')
        vocab = file.read().split()

        index += 1

        for word in raw_tweet:
            if word in vocab:
                vector[index] += 1

    data.append(vector)

# Storing feature vector
f = open('SVM/training_vectors', 'wb')
pickle.dump(data, f)
f.close()