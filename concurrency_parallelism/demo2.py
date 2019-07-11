#!/usr/bin/env python
# encoding: utf-8

"""
@author: Andy Cheng
@license: Apache Licence 
@file: demo2.py
@time: 2019/6/26 22:41
@desc: multi thread
"""
import concurrent.futures as futures
import requests
import time


def download(url):
    resp = requests.get(url)
    print(resp.status_code)


def download_all(sites):
    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download, sites)


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
