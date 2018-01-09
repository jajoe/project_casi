# coding: utf-8

import json
import urllib2
import string
import random

randomAlphabet = string.letters + "0123456789"

def createIdProxy(sizeId = 16):
    idProxy = ""
    for i in range(sizeId):
        idProxy += random.choice(string.letters)
    return idProxy

def sendTweet(tweet):
    idProxy = createIdProxy()
    data = {"idProxy": idProxy,"tweet": tweet, "uri":"http://localhost:4242/answer"}

    req = urllib2.Request("http://localhost:10042/tweet")
    req.add_header('Content-Type', 'application/json')

    res = urllib2.urlopen(req, json.dumps(data))
    return idProxy

smartProxy = "" # will contain lines "num line in the file 'tweets';idProxy\n"

with open("tweets", "r") as f:
    tweets = f.read().split("\n")
    for i in range(len(tweets)):
        if(len(tweets[i]) > 1):
            try:
                idProxy = sendTweet(tweets[i])
                smartProxy += str(i) + ";" + str(idProxy) + "\n"
            except Exception as e:
                print("error with the tweet num "+str(i))
                print(e)
        else:
            print("tweet num "+str(i)+" is empty")
    outputFile = open("smartProxy.csv", "w")
    outputFile.write(smartProxy)
    outputFile.close()

        
