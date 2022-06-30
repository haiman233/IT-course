# -*- coding: utf-8 -*-

import jieba
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import bs4
import requests

#爬取商品标题数据
url = 'https://re.taobao.com/search?keyword=%E8%BF%9B%E5%8F%A3%E9%9B%B6%E9%A3%9F&catid=50010550&refpid=619362_1007&_input_charset=utf8&clk1=b93e1915c335dd925dfcbf24ae696b12&spm=a21bo.2017.201874-p4p.7.5af911d9f5vIK4'      # 网址
payload = {'SearchText': 'taob', 'page': '1', 'ie': 'utf8', 'g': 'y'}  # 字典传递url参数
title = []
# 爬取商品标题
for i in range(0, 10):        # 循环10次，就是10个页面的商品数据
        payload['page'] = i    # 此处为页码，根据网页参数具体设置
        resp = requests.get(url, params=payload)
        soup = bs4.BeautifulSoup(resp.text, "html.parser")
        # print(resp.url)          # 打印访问的网址
        resp.encoding = 'utf-8'  # 设置编码
        # 标题
        all_title = soup.find_all('span', class_="title")
        for j in all_title:
            soup_title = bs4.BeautifulSoup(str(j), "html.parser",)
            title.append(soup_title.span.string)
print(title)

#商品标题词云图
pic_mask=np.array(Image.open("ty.jpg"))#获取词云形状的图片
print(len(title))
for i in title:
       words = jieba.lcut(i)
       new_text=' '.join(words)
wordcloud=WordCloud(font_path='simhei.ttf',background_color="white", #显示的字体和背景颜色
                    max_words=100,#出现次数最多的前100个分词
                    max_font_size=150,#显示的最大字号
                    random_state=10,#分词颜色的随机配色方案数量
                    mask=pic_mask) #词云形状
w=wordcloud.generate(new_text)#传入分词列表
plt.imshow(w)#绘制词云图
plt.axis("off")#关闭坐标
plt.show()#显示词云图
