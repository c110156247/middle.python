num=input("輸入數字")

list1=list(num)
list1.sort(reverse=True)
max=""
for i in range(0,len(list1)):
    max=max+list1[i]
    ans1=int(max)

min=""
list2=list(num)
list2.sort()   
for j in range(0,len(list2)):
    min=min+list2[j]
    ans2=int(min)
print("最大數列與最小數列差值為:"+str(ans1-ans2))    