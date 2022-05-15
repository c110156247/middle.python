km=float(input('輸入路程公里數(km):'))
price=75
while(km>1.5):
    price+=5
    km-=0.25

print('所需車資為:'+str(price))