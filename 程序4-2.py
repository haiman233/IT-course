s = input("请输入购买笔记本的数量（多少本）：")
s = int(s)
p = float(input("请输入笔记本的单价（每本多少元）："))
if s < 6:    
    j = 1.0
if s >= 6 and s <= 10: 
    j = 0.9
if s >= 11:    
    j = 0.8
t = s*p*j
print("总金额数为:",t,"元")
