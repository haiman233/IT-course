#for-while 循环嵌套

print(2,end=" ")
for k in range(3,101):
    find=False
    i=2
    while(i<k):
        if k%i==0:
            find=True
        i+=1
    if find==false:
        print(k,end=" ")