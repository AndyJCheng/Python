#!/usr/bin/env python
# encoding: utf-8
"""
@author: andy cheng
@license: Apache Licence 
@file: github.py
@time: 2018/7/2 22:59
@doc: https://github.com/jian-en/imooc-requests
"""
import requests
import json
url = 'https://api.github.com'


def build_uri(endpoint):
    return '/'.join([url, endpoint])


def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)


def request_method():
    response = requests.get(build_uri('users/AndyJCheng'))
    print(json.dumps(json.loads(response.text), indent=4))


def request_parameters():
    response = requests.get(build_uri('users'), params={'since': 11})
    print(better_print(response.text))
    print(response.url)


if __name__ == '__main__':
    request_parameters()
