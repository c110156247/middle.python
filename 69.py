secret=list(input('輸入摩斯密碼：'))
n=5
result=[secret[i:i+n] for i in range(0,len(secret),n)]
print(result)
for j in range(len(result)):
    if result[j]==['.', '-', '-', '-', '-']:
        print(1,end='')
    elif result[j]==['.', '.', '-', '-', '-']:
        print(2,end='')   
    elif result[j]==['.', '.', '.', '-', '-']:
        print(3,end='')
    elif result[j]==['.', '.', '.', '.', '-']:
        print(4,end='')  
    elif result[j]==['.', '.', '.', '.', '.']:
        print(5,end='')   
    elif result[j]==['-', '.', '.', '.', '.']:
        print(6,end='')
    elif result[j]==['-', '-', '.', '.', '.']:
        print(7,end='')
    elif result[j]==['-', '-', '-', '.', '.']:
        print(8,end='')   
    elif result[j]==['-', '-', '-', '-', '.']:
        print(9,end='')
    elif result[j]==['-', '-', '-', '-', '-']:
        print(0,end='')   