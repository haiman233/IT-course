print("请输入三种笔记本的优惠金额数（元）：")
a,b,c = input().split()
a = float(a)
b = float(b)
c = float(c)
if a > b: 
   m = a
else: 
   m = b
if c > m:
    m = c
print("优惠金额数最大的为：", m, "元")
