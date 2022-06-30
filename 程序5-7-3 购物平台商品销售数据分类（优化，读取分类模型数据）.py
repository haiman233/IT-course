# -*- coding: utf-8 -*-
#高斯朴素贝叶斯
import numpy as np
import pandas as pda
from sklearn.naive_bayes import GaussianNB
#构建分类模型
fname="model.csv"
dataf=pda.read_csv(fname,encoding="gbk")
data=dataf.as_matrix()
X=[]
Y=[]
for values in data:
    X.append(values[1:4]) #获取第2-4列的特征值
    Y.append(values[0]) #获取第1列的分类值
clf = GaussianNB().fit(X, Y)
#对未分类数据分类
print(clf.predict([[128.8,158,4.7]]))
