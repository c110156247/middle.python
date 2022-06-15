works=[]
while True:
    work=input('輸入事項(若無,請輸入end)')
    works.append(work)
    if work =='end':
        print('')
        break
del works[-1]    
for i in range(len(works)):
    print(str(i+1)+'.'+works[i])