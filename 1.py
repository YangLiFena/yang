# -*- coding: utf-8 -*-
# 思路：1、分词；2、列出所有词；3、分词编码；4、词频向量化；5、套用余弦函数计量两个句子的相似度。
# import sys
import jieba
import jieba.analyse
# 机器学习包
from sklearn.metrics.pairwise import cosine_similarity


class CosineSimilarity(object):

    # 余弦相似度
    def __init__(self, content_y1, content_y2):
        self.s1 = content_y1
        self.s2 = content_y2

    @staticmethod
    def extract_keyword(content):  # 提取关键词
        # 切割
        seg = [i for i in jieba.cut(content, cut_all=True) if i != '']  # 全模式分词
        # print(seg)
        # 提取关键词
        keywords = jieba.analyse.extract_tags("/".join(seg), topK=200, withWeight=False)
        return keywords

    @staticmethod
    def one_hot(word_dict, keywords):  # oneHot编码
        # cut_code = [word_dict[word] for word in keywords]
        cut_code = [0] * len(word_dict)
        for word in keywords:
            cut_code[word_dict[word]] += 1
        return cut_code

    def main(self):
        # 去除停用词
        # jieba.analyse.set_stop_words('orig.txt')
        # 提取关键词
        keywords1 = self.extract_keyword(self.s1)
        keywords2 = self.extract_keyword(self.s2)
        # 使用set函数创建集合并进行词的并集
        union = set(keywords1).union(set(keywords2))
        # 字典编码
        word_dict = {}
        i = 0
        for word in union:
            word_dict[word] = i
            i += 1
        # oneHot编码
        s1_cut_code = self.one_hot(word_dict, keywords1)
        s2_cut_code = self.one_hot(word_dict, keywords2)
        # 余弦相似度计算
        sample = [s1_cut_code, s2_cut_code]
        # 除零处理
        try:
            sim = cosine_similarity(sample)
            return sim[1][0]
        except Exception as e:  # 捕获所有错误类型
            print(e)  # 打印异常到屏幕
            return 0.0

# 测试
if __name__ == '__main__':
    with open('E:\\软工实践\\sim_0.8\\orig.txt', 'r', encoding='utf-8') as x1, \
            open('E:\\软工实践\\sim_0.8\\orig_0.8_dis_10.txt', 'r', encoding='utf-8')as x2:
        content_x1 = x1.read()
        x1.close()
        content_x2 = x2.read()
        x2.close()
        similarity = CosineSimilarity(content_x1, content_x2)
        similarity = similarity.main()
        print('相似度: %.2f%%' % (similarity * 100))
