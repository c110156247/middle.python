booKcaseA=['飢餓遊戲','解憂雜貨店','小王子','傲慢與偏見','麥田捕手','123']
booKcaseB=['吃飽遊戲','煩惱雜貨店','小公主','偏見與傲慢','蚊子殺手','456']
found=input('輸入欲租借書籍')
if (found in booKcaseA) ==True or (found in booKcaseB) ==True:
    if found in booKcaseA:
     ans=booKcaseA.index(found)
     print('在書架A的第'+str(ans+1)+'本')
    elif found in booKcaseB:
      ans=booKcaseB.index(found)
      print('在書架B的第'+str(ans+1)+'本')  
else:
    print("查無此書籍")
