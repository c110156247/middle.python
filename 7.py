telecase=int(input("輸入方案:186 or 386 or 586 or 986:"))
time=int(input("輸入時間"))
if telecase==386:
    price=time*0.08
    if price<=386:
        print('通話費為:386')
    elif price>386:
        if price<=386*2:
            print('通話費為:',round(price*0.8))
        elif price>386*2:
            print('通話費為:',round(price*0.7)) 
elif telecase==186:            
    price=time*0.09
    if price<=186:
        print('通話費為:186')
    elif price>186:
        if price<=186*2:
            print('通話費為:',round(price*0.9))
        elif price>186*2:
            print('通話費為:',round(price*0.8)) 
elif telecase==586:            
    price=time*0.07
    if price<=586:
        print('通話費為:586')
    elif price>586:
        if price<=586*2:
            print('通話費為:',round(price*0.7))
        elif price>186*2:
            print('通話費為:',round(price*0.6))    
elif telecase==986:            
    price=time*0.06
    if price<=986:
        print('通話費為:986')
    elif price>986:
        if price<=986*2:
            print('通話費為:',round(price*0.6))
        elif price>186*2:
            print('通話費為:',round(price*0.5))                          