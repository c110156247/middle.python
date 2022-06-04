total=0
n=int(input('輸入n值：'))
k=int(input('輸入k值：'))
match=n//k
mix=match//k
total+=n+match+mix
print('煙鬼可以抽'+str(total)+'紙菸')