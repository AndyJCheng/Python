#!/usr/bin/env python
# encoding: utf-8
"""
@author: Andy Cheng
@license: Apache Licence 
@file: demo01.py
@time: 2019/7/1 21:47
"""
from  pywifi import PyWiFi


def check_state():
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    print(iface.status())
    if iface.status() == 4:
        print('connected')
    else:
        print('broken')


def get_wireless():
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    for i in iface.scan_results():
        print(i.ssid, i.akm[0])


get_wireless()

