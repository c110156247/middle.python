n=int(input("輸入n"))
print(n)
while True:
    if n%2==1:
        n=n*3+1
        print(n)
    elif n%2==0:
        n=n/2
        print(n)
    if n==1:
        print(n)
        break        