n1_list=[]
n2_list=[]
n1=int(input('輸入第一個判斷數字'))
n2=int(input('輸入第二個判斷數字'))
if n1-n2 ==2 or n2-n1 ==2:
        for i in range(1,n1+1):
            if n1%i==0:
                n1_list.append(i)
        #n1_count=int(len(n1_list))        
        for j in range(1,n2+1):
            if n2%j==0:
                n2_list.append(j)
        #n2_count=int(len(n2_list)) 
        if len(n1_list)==len(n2_list):
            print('Y')
        else:
            print('N')                 
elif (n1==1 or n2==1) and (n1==2 or n2==2):
    print('N')
elif (n1==2 or n2==2) and (n1==3 or n2==3):
    print('N')