# coding: utf-8

import json
import urllib2
import time
import os
import sys
from os import listdir
from os.path import isfile, join
import nltk

reload(sys) 
sys.setdefaultencoding('utf8')
nltk.download('punkt')
pathSource = "/tmp/tweet/"
pathDest = "/tmp/tweet2/"

def send_result(idProxy, result, computationTime):
    data = {"idProxy": idProxy,"result": result, "time": computationTime}

    req = urllib2.Request("http://localhost:4242/answer")
    req.add_header('Content-Type', 'application/json')

    res = urllib2.urlopen(req, json.dumps(data))

def separate_words(tweet):
    tweet = unicode(tweet, errors='ignore')
    return nltk.word_tokenize(tweet)

def ponderation_list_words(listWords):
    ponderation = 0
    for word in listWords:
        if word in dictionary:
            ponderation += dictionary[word]
    return ponderation

def evaluate_tweet(tweet):
    words = separate_words(tweet)
    ponderation = ponderation_list_words(words)
    return ponderation

def load_dictionary():
    dictionary = {}
    with open("dictionary.csv", "r") as f:
        lines = f.read().split("\n")
        for line in lines:
            elements = line.split(";")
            if len(elements) == 2:
                dictionary[elements[0]] = int(elements[1])
    return dictionary

def watch_and_move():
    while True:
        files = [f for f in listdir(pathSource) if isfile(join(pathSource, f))]   
        for nameFile in files:
            f = open(pathSource+nameFile, "r")
            content = f.read()
            elements = content.split("\n")
            tic = time.clock()
            ponderation = evaluate_tweet(elements[0])
            timeComputation = time.clock() - tic 
            try:
                send_result(nameFile.replace(".txt", ""), ponderation, timeComputation)
            except Exception as e:
                print(e)
            os.rename(pathSource+nameFile, pathDest+nameFile)
        time.sleep(0.01)

dictionary = load_dictionary()
watch_and_move()

# below, test of evaluate_tweet
"""
tweet = "The woman stushgyal_yoly and I about to watch Iron Man 3 #ironman #marvel #geek #superhero #avengers http://t.co/CCHfImAVJuMane @CLowe_ is the guy who goes to see iron man 3 w/o me me....wtf bro"
dictionary = load_dictionary()
ponderation = evaluate_tweet(tweet)
print(ponderation)
"""

# below, test of send_result
"""
try:
    send_result("aaaaccccrrrrllll", 10, 0.001)
except Exception as e:
    print(e)
"""
