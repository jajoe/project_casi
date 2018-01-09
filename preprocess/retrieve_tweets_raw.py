from os import listdir
from os.path import isfile, join
import sys

mypath = "tweets_raw/"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
tweets = []
for myfile in onlyfiles:
    with open(mypath+myfile, "r") as f:
        content = f.read()
        elements = content.split("\n")
        for tweet_raw in elements:
            if len(tweet_raw) > 1:
                try:
                    tweet = eval(tweet_raw.replace("null", "None").replace("false", "False").replace("true", "True"))
                    tweet = tweet["text"]
                    tweets.append(tweet)
                except:
                    print("Unexpected error:", sys.exc_info()[0])
outputFile = open("tweets", "w")
outputFile.write("\n".join(tweets))
outputFile.close()
