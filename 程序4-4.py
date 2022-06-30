x = int(input("输入经费的值: "))
k = x // 4
y = x % 4
if y==0: 
   m=0 
   n=0
elif y==1:
    m=0
    n=1
    k=k-1
elif y==2:
    m=1 
    n=0
    k=k-1
elif y==3:
    m=1
    n=1
    k=k-2
print("6元的笔记本为: %d 本" % m)
print("5元的笔记本为: %d 本" % n)
print("4元的笔记本为: %d 本" % k)
