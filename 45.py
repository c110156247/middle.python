m=int(input('輸入月份'))
d=int(input("輸入日期"))
ans=(m*2+d)%3
if ans==0:
    print('普通')
elif ans==1:
    print('吉')
elif ans==2:
    print('大吉')
        