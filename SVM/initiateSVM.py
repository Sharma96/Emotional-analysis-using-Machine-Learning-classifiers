from SVM import getTweets, createTestSet, svmImplementation


# Main execution of the entire prediction model
def main(userName):

    getTweets.getTweets(userName)
    createTestSet.createTestSet(userName)
    emotion = svmImplementation.svmImplementation(userName)
    return emotion