# -*- coding: utf-8 -*-

#通过聚类分析客户价值
import csv
import pandas as pda
import numpy as npy
import matplotlib.pylab as pyl
from sklearn.cluster import KMeans

fname="company.csv"
dataf=pda.read_csv(fname,encoding="gbk")
x=dataf.as_matrix()

kms=KMeans(n_clusters=3)
y=kms.fit_predict(x)
print(y)

#年龄-消费金额图，消费时间-消费金额图，年龄-消费时间图
for i in range(0,len(y)):
    if(y[i]==0):
        print(str(i)+"0")
        pyl.subplot(2,3,1)
        #年龄-消费金额图
        pyl.plot(dataf.iloc[i:i+1,0:1].as_matrix(),dataf.iloc[i:i+1,1:2].as_matrix(),"*r")
        pyl.subplot(2,3,2)
        #消费时间-消费金额图
        pyl.plot(dataf.iloc[i:i+1,2:3].as_matrix(),dataf.iloc[i:i+1,1:2].as_matrix(),"*r")
        pyl.subplot(2,3,3)
        #年龄-消费时间图
        pyl.plot(dataf.iloc[i:i+1,0:1].as_matrix(),dataf.iloc[i:i+1,2:3].as_matrix(),"*r")

    elif(y[i]==1):
        print(str(i)+"1")
        pyl.subplot(2,3,1)
        #年龄-消费金额图
        pyl.plot(dataf.iloc[i:i+1,0:1].as_matrix(),dataf.iloc[i:i+1,1:2].as_matrix(),"sy")
        pyl.subplot(2,3,2)
        #消费时间-消费金额图
        pyl.plot(dataf.iloc[i:i+1,2:3].as_matrix(),dataf.iloc[i:i+1,1:2].as_matrix(),"sy")
        pyl.subplot(2,3,3)
        #年龄-消费时间图
        pyl.plot(dataf.iloc[i:i+1,0:1].as_matrix(),dataf.iloc[i:i+1,2:3].as_matrix(),"sy")
    elif(y[i]==2):
        print(str(i)+"2")
        pyl.subplot(2,3,1)
        #年龄-消费金额图
        pyl.plot(dataf.iloc[i:i+1,0:1].as_matrix(),dataf.iloc[i:i+1,1:2].as_matrix(),"pb")
        pyl.subplot(2,3,2)
        #消费时间-消费金额图
        pyl.plot(dataf.iloc[i:i+1,2:3].as_matrix(),dataf.iloc[i:i+1,1:2].as_matrix(),"pb")
        pyl.subplot(2,3,3)
        #年龄-消费时间图
        pyl.plot(dataf.iloc[i:i+1,0:1].as_matrix(),dataf.iloc[i:i+1,2:3].as_matrix(),"pb")
pyl.show()
