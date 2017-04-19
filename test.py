from __future__ import absolute_import, unicode_literals
__version__ = '0.38'
__license__ = 'MIT'
import re
from jieba._compat import *
def cut(sentence):
    sentence = strdecode(sentence)
    test = re.compile("[\u4E00-\u9FD5]+", re.U)
    glist = test.split(sentence)
    for i in glist:
        print(i)