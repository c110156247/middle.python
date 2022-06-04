n1=list(input('輸入第一組數字：'))
n2=list(input('輸入第二組數字：'))
a=0
b=0
for i in range(len(n1)):
    if n1[i]==n2[i]:
        a+=1
    else:
        b+=1
if a==len(n1):
    print("%dA%dB" %(a,b)+'全對')
else:            
    print("%dA%dB" %(a,b)+'加油')