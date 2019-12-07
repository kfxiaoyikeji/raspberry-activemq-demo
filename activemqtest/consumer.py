# -*- coding: utf-8 -*-
import conn
import signal


class TestListener(object):
    def on_message(self,headers,message):
        print('headers: %s' % headers)
        print('message: %s' % message.decode('utf8'))

def exit(signum,frame):
    conn.closeConn()

signal.signal(signal.SIGINT,exit)
signal.signal(signal.SIGTERM,exit)

# mqType = 0,listenerName = '',listenerObj = None,subscribe = ''
conn.config(1,'TestListener',TestListener(),conn.topic_name)

while True:
    pass
    
