#!/usr/bin/env python
import pygelf
import requests
client = pygelf.Client()

r = requests.get('http://www.google.com/')
response = r
client.send(str(r), "local1")
