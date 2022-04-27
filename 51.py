str=input('輸入自傳')
repeat=[]
for i in str:
    ans=str.count(i,0,len(str))
    if ans>1 and i not in repeat:
        repeat.append(i)
print(repeat)        