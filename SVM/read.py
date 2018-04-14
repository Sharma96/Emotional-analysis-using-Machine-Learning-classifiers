import pickle

data = open('training_tweets','rb')
output = pickle.load(data)

print(len(output))
for i in range(0,100):
    print(output[i])