#!/usr/bin/env python
# encoding: utf-8
"""
@author: andy cheng
@license: Apache Licence 
@file: server.py
@time: 2018/8/4 22:45
"""

import socket

sk = socket.socket()
ip_port = ('localhost', 9998)
sk.bind(ip_port)
sk.listen(5)
while True:
    conn, address = sk.accept()
    while True:
        with open('receive.txt', 'ab') as f:
            data = conn.recv(1024)
            if data == b'quit':
                break
            f.write(data)
        print('receive file done')
sk.close()
