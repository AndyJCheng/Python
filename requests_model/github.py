#!/usr/bin/env python
# encoding: utf-8
"""
@author: andy cheng
@license: Apache Licence 
@file: github.py
@time: 2018/7/2 22:59
"""
import requests
import json
url = 'https://api.github.com'


def build_uri(endpoint):
    return '/'.join([url, endpoint])


def request_method():
    response = requests.get(build_uri('users/AndyJCheng'))
    print(json.dumps(json.loads(response.text), indent=4))


if __name__ == '__main__':
    request_method()
