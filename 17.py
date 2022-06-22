n1,m1=input('輸入第一個矩陣(空白隔開)為：').split(" ")
nm1=[]
for i in range(int(n1)):
    nm1.append(input('輸入第一個矩陣值第'+str(i+1)+'列的值').split(" "))
print(nm1)

n2,m2=input('輸入第二個矩陣(空白隔開)為：').split(" ")
nm2=[]
for i in range(int(n2)):
    nm2.append(input('輸入第二個矩陣值第'+str(i+1)+'列的值').split(" "))
print(nm2)
ans=[]
if n1==n2 and m1==m2:
    for i in range(len(nm1)):
        for j in range(len(nm2)):
            ans.append(int(nm1[i][j])+int(nm2[i][j]))
    print(ans)        
else:
    print("兩矩陣無法相加")                    