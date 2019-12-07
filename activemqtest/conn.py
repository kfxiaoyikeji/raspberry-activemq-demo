# -*- coding: utf-8 -*-
import stomp

topic_name = '/topic/test'
host = '127.0.0.1'
port = 61613
user = 'test'
password = '123456'

_conn = stomp.Connection12([(host,port)])

def config(mqType,listenerName,listenerObj,subscribe):
    if mqType == 1: # 1 is consumer level
        _conn.set_listener(listenerName,listenerObj)
        _conn.connect(user,password,wait = True)
        _conn.subscribe(destination = subscribe,id = 'test',ack='auto')
    else:
        _conn.connect(user,password,wait = True)
    
    #_conn.start() # the connect is added start func,so,del start code

    
    

    


def sendToTopic(msg):
    print('send msg is'+ msg)
    _conn.send(topic_name,msg)

def closeConn():
    _conn.disconnect()

def test():
    print('conn test function')