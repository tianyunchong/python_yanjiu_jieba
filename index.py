#!python.exe
# coding=utf-8
import jieba


if __name__ == "__main__":
    tstr = '供应马鞍山8V皮带轮 8V皮带轮规格参数 8V皮带轮厂家'
    seg_list = jieba.cut(tstr, cut_all=True)
    print("Full Mode: " + " ".join(seg_list))  # 全模式
