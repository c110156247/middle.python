num=int(input("輸入電費"))
if num<=120 :
    totals=num*2.10
    totalns=num*2.10
elif 121<num<=330:
    totals=120*2.10+(num-120)*3.02
    totalns=120*2.10+(num-120)*2.68   
elif 331<num<=500:
    totals=120*2.10+210*3.02+(num-330)*4.39 
    totalns=120*2.10+210*2.68+(num-330)*3.61
elif 501<num<=700:
    totals=120*2.10+210*3.02+170*4.39+(num-500)*4.97
    totalns=120*2.10+210*2.68+170*3.61+(num-500)*4.01
elif num>=701:
    totals=120*2.10+210*3.02+170*4.39+200*4.97+(num-700)*5.63
    totalns=120*2.10+210*2.68+170*3.61+200*4.01+(num-700)*4.50    
print("summer months:"+str(totals))
print("non-summer months:"+str(totalns))    