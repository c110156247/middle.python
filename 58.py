x=10
y=[]
z=[]
for i in range(1,x+1):
    num=int(input("輸入第%d個數字" %(i)))
    y.append(num)
    y.sort(reverse=True)
    z.append(num)
    z.sort()
print("最大的3個數字為：%d,%d,%d" %(y[0],y[1],y[2]))    
print("最小的3個數字為：%d,%d,%d" %(z[0],z[1],z[2]))

