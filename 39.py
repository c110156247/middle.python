for i in range(4):
    for j in range(3-i):
        print(" ",end='')
    for k in range(i+1):
        print('*',end='')
    for l in range(i):
        print('*',end='')
    print()
for i in range(3,0,-1):
    for j in range(3-i+1):
        print(" ",end='')
    for k in range(i):
        print("*",end='')
    for l in range(i-1):
        print("*",end='')
    print()                            