num=list(map(int,input().split()))
check=int(len(num))/2
for i in range(len(num)):
    if num.count(num[i]) > check:
        ans=num[i]
        print("過半原素為:"+str(ans))
        break
    else:
        print("no")
        break