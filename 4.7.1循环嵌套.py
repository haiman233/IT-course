#for 循环嵌套

for i in range(0,100//5):
    for j in range(0,100//3):
        k=100-i-j
        if i*5+j*3+k/3==100:
            print("公鸡",i,"母鸡",j,"小鸡",k)