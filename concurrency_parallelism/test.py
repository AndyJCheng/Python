#!/usr/bin/env python
# encoding: utf-8
"""
@author: andy cheng
@license: Apache Licence 
@file: test.py
@time: 2018/7/16 22:16
"""
# import threading
from multiprocessing.dummy import Pool as ThreadPool


def run(name):
    print(name)


# t = threading.Thread(target=run, args=('aaa', ))
# t.start()

pool = ThreadPool()

lst = list(range(99999))
pool.map(run, lst)
pool.close()
pool.join()
