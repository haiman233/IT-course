"""
7.小组最终决定购买单价分别为1.8元的笔记本、1.9元的笔、2.1元的小饰品作为活动的奖品
和纪念品，每一种物品至少买100件，并且尽可能地用完1000元经费。如何设计方案，才能
实现购买物品数量最多？如数量相同的情况下余额最小的方案为最佳，则最佳方案中每一
种物品的数量是多少？余额是多少？
"""

x1=100  #1.8元笔记本的数量
y1=100  #1.9元笔的数量
z1=100  #2.1元小饰品的数量
s=300   # 礼物总数量
r=1000-(100*1.8+100*1.9+100*2.1) #余额

for x in range(100,556):  # 全部经费最多买555本笔记本，所以循环范围为100至556

    for y in range(100,527): # 全部经费最多买526支笔，所以循环范围为100至527

        for z in range(100,477): # 全部经费最多买476个小饰品，所以循环范围为100至477

            if 1.8*x+1.9*y+2.1*z <=1000:
                
                if x+y+z>s: # 如果此时三种纪念品的数量之和大于纪念品数量s
                    s=x+y+z #那么更改s的值为现在三种纪念品的数量之和
                    r=1000-(1.8*x+1.9*y+2.1*z) #计算余额
                    x1=x #更新三种纪念品的数量
                    y1=y
                    z1=z
                    
                if x+y+z==s and r>=1000-(1.8*x+1.9*y+2.1*z):  #如果此时三种纪念品数量之和等于之前记录的纪念品数量，且余额
                                                              #比之前记录的余额r要小

                    s=x+y+z  #那么更改s的值为现在三种纪念品的数量之和
					r=1000-(1.8*x+1.9*y+2.1*z)
                    x1=x   #更新三种纪念品的数量
                    y1=y
                    z1=z
            else:
                    break  #当1.8*x+1.9*y+2.1*z>1000，则可以退出循环，避免循环空转而浪费时间

print("符合条件的最优方案为：")
print("单价1.8元的物品数量是：",x1)
print("单价1.9元的物品数量是：",y1)
print("单价2.1元的物品数量是：",z1)
print("共买到的礼物总数量为：",s)
print("余额还剩：",r,"元")
