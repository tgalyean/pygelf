#!/usr/bin/env python
import threading
import requests
import time
import datetime
import pygelf

stuff = open('file.txt', 'r')
client = pygelf.Client()

class ThreadClass(threading.Thread):
  def run(self):
    now = datetime.datetime.now()
    thread_name = str(self.getName())
    exec_time = str(now)
    print thread_name + " " + exec_time
    send()

def send():
    for item in stuff:
        print item
        client.send(item.strip('\n'), "local1")

def start():
    for i in range(5):
        t = ThreadClass()
        t.start()

start()
