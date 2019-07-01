#!/usr/bin/env python
# encoding: utf-8

"""
@author: Andy Cheng
@license: Apache Licence 
@file: demo1.py
@time: 2019/6/26 22:31
@desc: this is single thread example
"""
import requests
import time


def download(url):
    resp = requests.get(url)
    print(resp.status_code)


def download_all(sites):
    for site in sites:
        download(site)


sites = ['https://github.com',
         'https://github.com',
         'https://github.com',
         'https://github.com',
         'https://github.com',
         'https://github.com',
         ]
start_time = time.perf_counter()
download_all(sites)
end_time = time.perf_counter()
print(end_time - start_time)
