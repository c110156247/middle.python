n=int(input('n筆資料'))
list1=[]
for i in range(n):
    n1=input('距離')
    list1.append(n1)
 
check=int(input("點位"))
check1=check-1

if check>len(list1):
    print('0')
else:
    print('第'+str(check)+'個點:'+list1[check1]) 