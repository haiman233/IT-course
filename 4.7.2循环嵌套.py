#while-for 循环嵌套

i=0
while(i<10):
    i+=1
    for j in range(1,i+1):
        print(i,"x",j,"=",i*j,sep="",end=" ")
        if i*j<10:
            print(" ",end="")
    print()
