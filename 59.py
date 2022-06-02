money=int(input('輸入金額(兌換最少硬幣和紙鈔100,50,10,5,1)：'))
x100=money//100
x50=money%100//50
x10=money%100%50//10
x5=money%100%50%10//5
x1=money%100%50%10%5
total=x100+x50+x10+x5+x1
print(total)