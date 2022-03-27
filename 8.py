num=input("輸入數字")
list1=list(num)
count=0
count1=0
for i in range(0,len(list1)):
    if list1.count(list1[i])> count:
         count=list1.count(list1[i])
         count1=list1[i]
print("最大出現次數的數字為:"+str(count1)+"出現次數為:"+str(count))
