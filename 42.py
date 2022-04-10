a=int(input('輸入a:'))
b=int(input('輸入b:'))
c=int(input('輸入c:'))
num=b**2-4*a*c
if num>0:
    x1=(-b + num**0.5) / 2*a
    x2=(-b - num**0.5) / 2*a
    print(x1,x2)
elif num==0:
    x1=-b/2*a
    print(x1)
elif num<0:
    print('無解')    