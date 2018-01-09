# coding: utf-8

import json
import urllib2

def sendResult(idProxy, result, computationTime):
    data = {"idProxy": idProxy,"result": result, "time": computationTime}

    req = urllib2.Request("http://localhost:4242/answer")
    req.add_header('Content-Type', 'application/json')

    res = urllib2.urlopen(req, json.dumps(data))

try:
    sendResult("aaaaccccrrrrllll", 10, 0.001)
except Exception as e:
    print(e)
