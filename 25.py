grades=[[70,80,90,80,100,80],[60,70,80,70,40,70],[30,50,40,60,50,40]]
test,students=input('輸入考試次數和學生數(6,3)：').split(" ")
y=input("輸入考試比率(空白隔開)：").split(" ")
for i in range(len(y)):
    y[i]=float(y[i])
ans=0
for i in range(int(students)):
    for j in range(int(test)):
            ans+=int(grades[i][j]*y[j])
print("全班總平均值為：%.2f" %(ans/int(students)))            