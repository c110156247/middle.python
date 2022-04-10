dict1={}
n=int(input('n筆資料'))
for i in range(n):
    name,num=map(str,input().split(' ')) 
    dict1[name]=num
for key,value in dict1.items():
    print(key+"牌得到",value+'面')