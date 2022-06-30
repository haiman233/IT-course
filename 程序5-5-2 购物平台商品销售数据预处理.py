# -*- coding: utf-8 -*-

import pymysql
import numpy as npy
import pandas as pda
import matplotlib.pylab as pyl
import matplotlib.pyplot as plt

#导入数据
conn=pymysql.connect(host="127.0.0.1",user="root",passwd="",db="taobao")
sql="select * from taobao"
data=pda.read_sql(sql,conn)

#数据清洗，发现和处理缺失值,如果销量为0的，修改为200
x=0
data["paynum"][(data["paynum"]==0)]=None
for i in data.columns:
    for j in range(len(data)):
        if(data[i].isnull())[j]: #如果为空即插值
            data[i][j]="200" # 空值插入200
            x+=1
print(x)


#异常值处理、画散点图（横轴：价格，纵轴：评论数）找到异常值、
data2=data.T
price=data2.values[2]
comt=data2.values[3]
plt.xlabel('price')        #显示X坐标标签
plt.ylabel('paynum')         #显示Y坐标标签
pyl.plot(price,comt,"o")
pyl.show()

#处理异常数据，销量大于100，价格大于65都处理掉
line=len(data.values)
col=len(data.values[0])
da=data.values
#删除处理法
x=0
for i in range(0,line):
     if(da[i][3]>100):#销量大于100
         continue
     elif(da[i][2]>65):#价格大于65
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
plt.ylabel('paynum')         #显示Y坐标标签
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
paynummax=da2[3].max()
paynummin=da2[3].min()
#极差
pricerg=pricemax-pricemin
paynumrg=paynummax-paynummin
#组距
pricedst=pricerg/13
paynumdst=paynumrg/13

#绘制价格直方图
#npy.arrange(最小,最大,组距)
pricesty=npy.arange(pricemin,pricemax,pricedst)
plt.xlabel('price')        #显示X坐标标签
plt.ylabel('number')         #显示Y坐标标签
pyl.hist(da2[2],pricesty)
pyl.show()


#绘制销量数直方图
paynumsty=npy.arange(paynummin,paynummax,paynumdst)
plt.xlabel('paynum')        #显示X坐标标签
plt.ylabel('number')         #显示Y坐标标签
pyl.hist(da2[3],paynumsty)
pyl.show()
