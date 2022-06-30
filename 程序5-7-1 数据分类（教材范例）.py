# -*- coding: utf-8 -*-
#高斯朴素贝叶斯
import numpy as np
from sklearn.naive_bayes import GaussianNB
X = np.array([[182.8,81.6,30],[180.4,86.1,29],[170.0,77.1,30],[180.4,74.8,28],
              [152.4,45.3,24],[167.6,68.0,26],[165.2,58.9,25],[175.2,68.0,27]])
Y = np.array([1,1,1,1,0,0,0,0])
clf = GaussianNB().fit(X, Y)
print(clf.predict([[182.8,58.9,26]]))