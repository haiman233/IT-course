# -*- coding: utf-8 -*-

import pymysql
import numpy as npy
import pandas as pda
import matplotlib.pylab as pyl
import matplotlib.pyplot as plt

#导入数据
conn=pymysql.connect(host="127.0.0.1",user="root",passwd="",db="csdn")
sql="select * from taob"
data=pda.read_sql(sql,conn)

#数据清洗，发现和处理缺失值
x=0
data["price"][(data["price"]==0)]=None
for i in data.columns:
    for j in range(len(data)):
        if(data[i].isnull())[j]: #如果为空即插值
            data[i][j]="64" # 空值插入64
            x+=1
print(x)


#异常值处理、找到异常值、画散点图（横轴：价格，纵轴：评论数）
data2=data.T
price=data2.values[2]
comt=data2.values[3]
plt.xlabel('price')        #显示X坐标标签
plt.ylabel('comt')         #显示Y坐标标签
pyl.plot(price,comt,"o")
pyl.show()

#处理异常数据，评论大于65，价格大于100都处理掉
line=len(data.values)
col=len(data.values[0])
da=data.values
#删除处理法
x=0
for i in range(0,line):
    for j in range(0, col):
         if(da[i][3]>65):#评论数大于65
             continue
         elif(da[i][2]>100):#价格大于100
             continue
         else:
             if(x==0):
                newda=da[i]
             else:
                newda=npy.row_stack((newda,da[i]))
             x+=1

da2=newda.T
price=da2[2]
comt=da2[3]
plt.xlabel('price')        #显示X坐标标签
plt.ylabel('comt')         #显示Y坐标标签
pyl.plot(price,comt,"o")
pyl.show()

#分布分析
#求最值
#计算极差
#组距：极差/组数
#绘制直方图

#求最值
pricemax=da2[2].max()
pricemin=da2[2].min()
commentmax=da2[3].max()
commentmin=da2[3].min()
#极差
pricerg=pricemax-pricemin
commentrg=commentmax-commentmin
#组距
pricedst=pricerg/13
commentdst=commentrg/13

#绘制价格直方图
#npy.arrange(最小,最大,组距)
pricesty=npy.arange(pricemin,pricemax,pricedst)
plt.xlabel('price')        #显示X坐标标签
plt.ylabel('number')         #显示Y坐标标签
pyl.hist(da2[2],pricesty)
pyl.show()

#绘制评论数直方图
commentsty=npy.arange(commentmin,commentmax,commentdst)
plt.xlabel('comt')        #显示X坐标标签
plt.ylabel('number')         #显示Y坐标标签
pyl.hist(da2[3],commentsty)
pyl.show()
