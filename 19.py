test=int(input('輸入資料量'))
for i in range(test):
    fa,ma,kid=input('輸入血型(空白隔開)為：').split(" ")
    if (fa=='a' and ma=='b') or (fa=='b' and ma=='a'):
        print('yes')
    elif(fa=='o' and ma=='o') or (fa=='o' and ma=='o'):
        if kid =='o':
            print('yes')
        else:
            print("IMPOSSIBLE")
    elif(fa=='o' and ma=='a') or (fa=='a' and ma=='o'):
        if kid =='o' or kid=='a':
            print('yes')
        else:
            print("IMPOSSIBLE")    
    elif(fa=='o' and ma=='b') or (fa=='b' and ma=='o'):
        if kid =='o' or kid=='b':
            print('yes')
        else:
            print("IMPOSSIBLE")    
    elif(fa=='o' and ma=='ab') or (fa=='ab' and ma=='0'):
        if kid =='o' or kid=='ab':
            print('yes')
        else:
            print("IMPOSSIBLE") 
    elif (fa=='a' and ma=='a'):
        if kid=='a' or  kid=='o':
            print('yes')  
        else:
            print("IMPOSSIBLE")          
    elif(fa=='a' and ma=='ab') or (fa=='ab' and ma=='a'):
        if kid =='a' or kid=='b' or kid=='ab':
            print('yes')
        else:
            print("IMPOSSIBLE") 
    elif (fa=='b' and ma=='b'):
        if kid=='b' or  kid=='o':
            print('yes')
        else:
            print("IMPOSSIBLE")  
    elif(fa=='b' and ma=='ab') or (fa=='ab' and ma=='b'):
        if kid =='a' or kid=='b' or kid=='ab':
            print('yes')
        else:
            print("IMPOSSIBLE")      
    elif (fa=='ab' and ma=='ab'):
        if kid=='a' or  kid=='b' or kid=='ab':
            print('yes')  
        else:
            print("IMPOSSIBLE")                              