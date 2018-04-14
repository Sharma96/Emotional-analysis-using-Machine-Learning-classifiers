import matplotlib.pyplot as plot
from sklearn import svm
import pickle
from collections import Counter

emotions = ['anger','anticipation','disgust','fear','joy','sad','surprise','trust']


def svmImplementation(userName):

    with open('SVM/training_vectors', 'rb') as f:
        emotion_vector = pickle.load(f)

    with open('SVM/training_tweets', 'rb') as f:
        temp = pickle.load(f)
        target_classes = []

        for i in range(0,len(temp)):
            target_classes.append(temp[i][0])

    # 'C' is the cost of classification
    classifier = svm.SVC(C=1, kernel='linear')
    classifier.fit(emotion_vector,target_classes)

    # Reading user tweets - merely for demonstration purpose
    f = open('SVM/UserData/%s_latest_tweets' % userName, 'rb')
    tweets = pickle.load(f)
    f.close()

    # Reading the prepared test vectors, produced using the user tweets
    f = open('SVM/UserData/%s_test_vectors' %userName, 'rb')
    vectors = pickle.load(f)
    f.close()

    # Output below
    result = []
    for i in range(0,len(tweets)):
        print('Tweet: ', tweets[i])
        print('Vectors: ', vectors[i])
        print('Emotion: ', classifier.predict([vectors[i]]))
        print('\n')
        result.extend(classifier.predict([vectors[i]]))

    # Counting the most occuring emotion
    count = Counter(result)
    res = list(count.most_common(1))

    # Returning the final emotion
    return res[0][0]

