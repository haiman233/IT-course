# -*- coding: utf-8 -*-

#通过聚类分析客户价值
import csv
import pandas as pda
import numpy as npy
import matplotlib.pylab as pyl
from sklearn.cluster import KMeans
#导入商品样本数据
fname="data_sample.csv"
dataf=pda.read_csv(fname,encoding="gbk")
x=dataf.as_matrix()
#聚类分析
kms=KMeans(n_clusters=3)
y=kms.fit_predict(x)
print(y)

#价格-销售量，评论-销售量，价格-评论
for i in range(0,len(y)):
    if(y[i]==0):
        print(str(i)+"0")
        pyl.subplot(2,3,1)
        #价格-销售量
        pyl.plot(dataf.iloc[i:i+1,0:1].as_matrix(),dataf.iloc[i:i+1,1:2].as_matrix(),"*r")
        pyl.subplot(2,3,2)
        #评论-销售量
        pyl.plot(dataf.iloc[i:i+1,2:3].as_matrix(),dataf.iloc[i:i+1,1:2].as_matrix(),"*r")
        pyl.subplot(2,3,3)
        #价格-评论
        pyl.plot(dataf.iloc[i:i+1,0:1].as_matrix(),dataf.iloc[i:i+1,2:3].as_matrix(),"*r")

    elif(y[i]==1):
        print(str(i)+"1")
        pyl.subplot(2,3,1)
        #价格-销售量
        pyl.plot(dataf.iloc[i:i+1,0:1].as_matrix(),dataf.iloc[i:i+1,1:2].as_matrix(),"sy")
        pyl.subplot(2,3,2)
        #评论-销售量
        pyl.plot(dataf.iloc[i:i+1,2:3].as_matrix(),dataf.iloc[i:i+1,1:2].as_matrix(),"sy")
        pyl.subplot(2,3,3)
        #价格-评论
        pyl.plot(dataf.iloc[i:i+1,0:1].as_matrix(),dataf.iloc[i:i+1,2:3].as_matrix(),"sy")
    elif(y[i]==2):
        print(str(i)+"2")
        pyl.subplot(2,3,1)
        #价格-销售量
        pyl.plot(dataf.iloc[i:i+1,0:1].as_matrix(),dataf.iloc[i:i+1,1:2].as_matrix(),"pb")
        pyl.subplot(2,3,2)
        #评论-销售量
        pyl.plot(dataf.iloc[i:i+1,2:3].as_matrix(),dataf.iloc[i:i+1,1:2].as_matrix(),"pb")
        pyl.subplot(2,3,3)
        #价格-评论
        pyl.plot(dataf.iloc[i:i+1,0:1].as_matrix(),dataf.iloc[i:i+1,2:3].as_matrix(),"pb")
pyl.show()
