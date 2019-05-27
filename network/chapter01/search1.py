#!/usr/bin/env python
# encoding: utf-8

"""
@author: Andy Cheng
@license: Apache Licence 
@file: search1.py
@time: 2019/3/10 15:59
"""
from pygeocoder import Geocoder

if __name__ == '__main__':
    add = '207 N.Defiance St, Archbold, OH'
    print(Geocoder.geocode(add)[0].coordinates)
