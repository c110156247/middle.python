num=int(input("輸入11<=n<=1000的數字"))
while True:
    if (num%2==0 and num%11==0):
        if(num%5!=0 and num%7!=0):
            print(str(num)+'為新公倍數?:'+'YES')
        else:
            print('')
    else:
        print('NO')
    break                