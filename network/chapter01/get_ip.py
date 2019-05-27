#!/usr/bin/env python
# encoding: utf-8

"""
@author: Andy Cheng
@license: Apache Licence 
@file: get_ip.py
@time: 2019/5/26 15:43
"""

import socket

if __name__ == '__main__':
    hostname = 'www.dunksky.top'
    addr = socket.gethostbyname(hostname)
    print(addr)
