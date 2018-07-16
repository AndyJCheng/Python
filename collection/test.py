#!/usr/bin/env python
# encoding: utf-8
"""
@author: andy cheng
@license: Apache Licence 
@file: test.py
@time: 2018/7/9 22:10
"""
from collections import namedtuple
from collections import deque
from collections import defaultdict
import logging
logging.basicConfig(level=logging.NOTSET,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
point = namedtuple('point', ('x', 'y'))
p = point(22, 33)
print(p.x, p.y)
logging.debug('this is namedtuple')

q = deque([1, 2, 3])
q.appendleft(0)
q.popleft()
print(q)
logging.info('this is deque')
d = defaultdict(lambda: None)
d['a'] = '123'
print(d['a'])
print(d['b'])
logging.error('this is defaultdict')
