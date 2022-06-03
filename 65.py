com=[]
friend_a=list(map(int,input().split(" ")))
friend_b=list(map(int,input().split(" ")))
for i in range(len(friend_a)):
    if friend_a[i] in friend_b:
        com.append(friend_a[i])
print(str(len(com))+'位共同好友')        