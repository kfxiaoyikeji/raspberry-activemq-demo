# -*- coding: utf-8 -*-
import time
import conn
import signal
import json

def exit(signum,frame):
    conn.closeConn()

signal.signal(signal.SIGINT,exit)
signal.signal(signal.SIGTERM,exit)

conn.config(0,'',None,'')

index = 1

jsonObj = {'username':'第三本个人诗集',
           'age':18
           }

while True:
    jsonObj['username'] = '第三本个人诗集'+ str(index) 
    conn.sendToTopic(json.dumps(jsonObj))
    index += 1
    time.sleep(3)
    
    
    
    
