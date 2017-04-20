#!/usr/bin/python2.7
# coding=utf-8
import jieba
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

if __name__ == "__main__":
    tstr = '供应马鞍山8V皮带轮 8V皮带轮规格参数 8V皮带轮厂家'
    seg_list = jieba.cut(tstr)
    print("Full Mode" + " ".join(seg_list))
