x=[]
for i in range(5):
    num=input("輸入數字")
    if num=='A' :
        num=1
    if num=='J' :
        num=11
    if num=='Q' :
        num=12
    if num=='K' :
        num=13        
    x.append(int(num))
print(x)
print(sum(x))     


