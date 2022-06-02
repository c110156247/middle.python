x=int(input('輸入整數(<10)：'))
for i in range(x+1):
    for j in range(1,i+1):
            c=i*j
            print(c,end=' ')
    print()        