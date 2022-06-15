ans=['red','blue','red','green']
chance=10
for i in range(10):
    color = (input('輸入顏色(空白隔開)'))
    colors= color.split()
    post=''
    if len(colors)==4:
        for j in range(len(ans)):
            if colors[j] == ans[j]:
                post+='1'
            elif colors[j] in ans:
                post+='2'
            else:
                post+='3'
        print(post)
        if post=='1111':
            print('正確答案')
            break
        else:
            print('你還有%d次機會'%(chance-1))
            chance-=1
    else:
        print('請輸入正確')
    if chance == 0:
        print('挑戰失敗')