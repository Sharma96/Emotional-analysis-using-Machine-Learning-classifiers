from secrets import *
import tweepy
from SVM import initiateSVM
from Recommendation import songRecommendation, movieRecommendation

auth = tweepy.OAuthHandler(ConsumerKey,ConsumerSecret)
auth.set_access_token(AccessToken, AccessTokenSecret)

api = tweepy.API(auth)


def prepareMessage(songs, movies):

    # Adding songs
    temp = ''
    limit = len(songs)
    i = 0

    for s in songs:

        i += 1
        if i < limit:
            temp += s + ', '
        else:
            temp += s

    temp = 'Music: ' + temp
    result = []
    result.append(temp[0:110])

    # Adding movies
    temp = ''
    limit = len(movies)
    i=0

    for m in movies:

        i += 1
        if i < limit:
            temp += m + ', '
        else:
            temp += m

    temp = 'Movies: ' + temp
    result.append(temp[0:115])

    return result

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):

        tweetText = status.text
        userName = status.user.screen_name
        statusID = status.id

        # Logging live data to the console
        print(tweetText, statusID)

        try:

            api.update_status('@%s you tweeted me, you shall be enlightened.' % userName, in_reply_to_status_id = statusID)

            emotion = initiateSVM.main(userName)
            songs = songRecommendation.recommendation(emotion)
            movies = movieRecommendation.recommendation(emotion)
            replyMessage = prepareMessage(songs, movies)

            if emotion == 'enjoyment':
                api.update_status('@%s you seem to be enjoying your day, very good.' % userName, in_reply_to_status_id = statusID)

                print(replyMessage[0])
                print(replyMessage[1])

                api.update_status('@%s %s' % (userName, replyMessage[0]), in_reply_to_status_id = statusID)
                api.update_status('@%s %s' % (userName, replyMessage[1]), in_reply_to_status_id = statusID)

                print('tweeted to %s' % userName, ' | ', emotion)

            else:

                api.update_status('@%s I would soon be giving you suggestions to feel better.' % userName, in_reply_to_status_id = statusID)

                print(replyMessage[0])
                print(replyMessage[1])

                api.update_status('@%s %s' % (userName, replyMessage[0]), in_reply_to_status_id = statusID)
                api.update_status('@%s %s' % (userName, replyMessage[1]), in_reply_to_status_id = statusID)

                print('tweeted to %s' % userName, ' | ', emotion)

        except tweepy.TweepError:
            pass

while True:

    # Object of the MyStreamListener class
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)

    # Listening to the twitter home timeline for tweets containing @EmotionalGuru mention
    myStream.filter(track = ['@EmotionalGuru'])

