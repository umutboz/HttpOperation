#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
## test
############################################################
## Author: Umut Boz
## Copyright (c) 2020, OneframeMobile, KoçSistem
## Email: oneframemobile@gmail.com
############################################################
## Version: 0.1.0
############################################################
from enums import MessageType
from enums import CodeLine
from log import Log
from environment import Environment
from httpOperation import HttpOperation

MESSAGE = MessageType()

CODE = CodeLine()

url = "https://petstore.swagger.io/v2/swagger.json"

#op = HttpOperation()
#print(op.request(url=url))

op = HttpOperation(url=url)
print(op.request())

import json
'''
 jsonData = json.loads(dataString)
            return jsonData
'''            
