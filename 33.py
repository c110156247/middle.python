from operator import index


total=0
num=[]
item=['國文','英文','微積分','體育','程式設計']
for i in range(len(item)):
    inscore=int(input('輸入成績'))
    num.append(inscore)
for scores in num:
    total=total+scores    
avg=total/len(item)
ans=round(avg,2)
print('平均分數:'+str(ans))
big=max(num)
bigindex=num.index(big)
print("最高分科目:"+str(item[bigindex])+str(num[bigindex])+'分')
small=min(num)
smallindex=num.index(small)
print("最低分科目:"+str(item[smallindex])+str(num[smallindex])+'分')