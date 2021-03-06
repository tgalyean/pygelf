#!/usr/bin/env python
import config
import socket
import json
import pycurl

class Client():
    def send(self,message,facility):
        # graylog instance hostname / Gelf HTTP port
        hostname = config.get('hostname')
        port = config.get('port')
        endpoint = 'http://' + hostname + ":" + port + "/gelf"
    
        # create json object to send to Graylog
        content = {
            "short_message": message, 
            "host": socket.gethostname(), 
            "facility": facility, 
            "_method":"Gelf HTTP",
        }
        try:
            c = pycurl.Curl()
            c.setopt(pycurl.URL, endpoint)
            c.setopt(pycurl.HTTPHEADER, ['Accept: application/json', 'Content-Type: application/json'])
            c.setopt(pycurl.POST, 1)
            c.setopt(pycurl.POSTFIELDS, json.dumps(content))
            # force HTTP 1.0 to bypass KeepAlive (Compliments of Lennart Koopmann)
            c.setopt(pycurl.HTTP_VERSION, pycurl.CURL_HTTP_VERSION_1_0)
            c.perform()
            c.close()
            print "Message logged via Gelf HTTP: " + json.dumps(content)
        except pycurl.error as e:
            print e

