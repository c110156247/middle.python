t=int(input('班級數'))
list1=[]
for i in range(t):
    human=input("輸入人數")
    list1.append(human)
list1.sort(reverse=True)
print('須購買'+list1[0]+'台電腦')    
      