# -*- coding: utf-8 -*-
#高斯朴素贝叶斯
import numpy as np
from sklearn.naive_bayes import GaussianNB
X = np.array([[105.9,230,4.9],[65.1,710,4.8],[15,276,4.8],[238,79,4.8],[29.9,735,4.7],
              [12.8,222,4.3],[18,62,4.6],[89,247,4.5],[162,585,4.5],[29,278,4.2]])
Y = np.array(['重要商品','重要商品','重要商品','重要商品','重要商品',
              '一般商品','一般商品','一般商品','一般商品','一般商品'])
clf = GaussianNB().fit(X, Y)
print(clf.predict([[128.8,158,4.7]]))