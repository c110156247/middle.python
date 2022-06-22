while True:
    n,m=input('輸入N,M(空白隔開)為：').split(" ")
    x=[]
    for i in range(int(n)):
        x.append(input('輸入矩陣值第'+str(i+1)+'列(有'+str(m)+'個數字'+'為：').split(" "))
    for i in range(int(m)):
        ans=[]
        for j in range(int(n)):
            ans.append(x[j][i])
        print('輸出矩陣值第'+str(i+1)+'列為：',ans)
    break        