a=int(input("輸入組數"))
print("組數為"+str(a))
sum=0
for i in range(1,a+1):
    b,c=map(int,input().split(' '))
    sum=b*250+c*175
    print("第"+str(i)+"組應收費用:"+str(sum))