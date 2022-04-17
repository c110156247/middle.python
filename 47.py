list1=[]
list2=[]
n=int(input('n筆資料'))
for i in range(n):
    name,num=map(str,input().split(' '))
    list1.append(name)
    list2.append(num) 
for i in range(n):
     print(list1[i]+'牌得到'+list2[i]+'面')