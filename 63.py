list1=[]
total=0
n=int(input('輸入一個整數'))
for i in range(1,n+1):
    if n%i==0:
        list1.append(i)
for j in range(len(list1)):
    total+=list1[j]
total-=n
if total==n:
    print('perfect') 
elif total>n:
    print('abundant')  
elif total<n:
    print('deficient')  