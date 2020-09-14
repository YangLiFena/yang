# -*- coding: utf-8 -*-
import sys

import jieba
import jieba.analyse


class CosineSimilarity(object):

    def __init__(self, content_y1, content_y2):
        self.s1 = content_y1
        self.s2 = content_y2

    @staticmethod
    def extract_keyword(content):  # 提取关键词
        # 分词
        seg = jieba.lcut(content, cut_all=True)
        print(seg)
        # 提取关键词
        keywords = jieba.analyse.extract_tags("/".join(seg), topK=200, withWeight=False)
        return keywords

    def main(self):
        # 提取关键词
        keywords1 = self.extract_keyword(self.s1)
        keywords2 = self.extract_keyword(self.s2)
        print(keywords1)  # 查看该函数提取关键词的结果
        print(keywords2)


if __name__ == '__main__':
    x1 = open(sys.argv[1], 'r', encoding='utf-8')
    x2 = open(sys.argv[2], 'r', encoding='utf-8')
    content_x1 = x1.read()
    x1.close()
    content_x2 = x2.read()
    x2.close()
    similarity = CosineSimilarity(content_x1, content_x2)
    similarity = similarity.main()
