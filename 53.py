namedata=[]
maildata=[]
x=int(input('輸入次數'))
for i in range(x):
    inname=input('輸入姓名')
    namedata.append(inname)
    inmail=input('輸入電子郵件')
    maildata.append(inmail)

name=input('輸入查詢姓名')
if name in namedata:
    ans=namedata.index(name)
    print(name+'電子郵件帳號為'+maildata[ans])

else:
    print("no")
