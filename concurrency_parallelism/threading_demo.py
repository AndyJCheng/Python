#!/usr/bin/env python
# encoding: utf-8
"""
@author: Andy Cheng
@license: Apache Licence 
@file: threading_demo.py
@time: 2019/7/11 20:53
"""
import threading
from time import sleep, ctime

loops = [4, 2]


def loop(loopn, wait):
    print('start %s' % loopn, 'at:' + ctime())
    sleep(wait)
    print('end %s' % loopn, 'at:' + ctime())


def main():
    threads = []
    for i in range(len(loops)):
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in range(len(loops)):
        threads[i].start()

    for i in range(len(loops)):
        threads[i].join()

    print('done at:' + ctime())


main()
