dict1={}
n=int(input('n筆資料'))
for i in range(n):
    name,num=map(str,input().split(' ')) 
    dict1[name]=num
print(dict1)
que=input('輸入查詢單字:')
answer=dict1.get(que)
if answer==None:
    print('無此單字')
else:
    print(que+'的中文為'+dict1.get(que))    