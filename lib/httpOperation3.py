#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
## HttpOperation
############################################################
## Author: Umut Boz
## Copyright (c) 2020, OneframeMobile, KoçSistem
## Email: oneframemobile@gmail.com
############################################################
## Version: 0.1.0
############################################################


# Built-in/Generic Imports
import os
import sys
#import requests
import urllib2
import ssl
import json

# Own modules
from abstract import Base
from enums import CODING
from enums import MESSAGETYPE


class HttpOperation(Base):
    _url = ""


    def __init__(self, url=None):
        Base.__init__(self)
        self._url = url

    def url(self):
        if self._url == None or not str(self._url).strip():
            return None
        else:
            return self._url

    def request(self,url=None):
        request_url = None
        if url != None:
            request_url = str(url)
        else:
            request_url = self.url()
        if request_url == None:
            Base.log(self, message="HttpOperation " + "request : "
                      + " \error : \n url cannot be None", messageType=MESSAGETYPE.ERROR)
            return
        print(request_url)
        try:
            resp = urllib2.urlopen(request_url)
            dataString = resp.read().decode('utf-8')
            jsonData = json.loads(dataString)
            return jsonData
        except urllib2.HTTPError as e:
            print('HTTPError = ' + str(e.code))
        except urllib2.URLError as e:
            print('URLError = ' + str(e.reason))
        except Exception as e:
            print('generic exception: ' + str(e))
        
