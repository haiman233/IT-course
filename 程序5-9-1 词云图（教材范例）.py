import jieba
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
pic_mask=np.array(Image.open("ty.jpg"))#获取词云形状的图片
text=open(r'kebiao.txt',encoding='utf8')#获取分词数据
mylist=list(text)
word_list=[" ".join(jieba.cut(sentence)) for sentence in mylist]
new_text=' '.join(word_list)
wordcloud=WordCloud(font_path='simhei.ttf',background_color="white", #显示的字体和背景颜色
                    max_words=500,#出现次数最多的前500个分词
                    max_font_size=150,#显示的最大字号
                    random_state=40,#分词颜色的随机配色方案数量
                    mask=pic_mask) #词云形状
w=wordcloud.generate(new_text)#传入分词列表
plt.imshow(w)#绘制词云图
plt.axis("off")#关闭坐标
plt.show()#显示词云图