com=[]
str_a=list(input('輸入字串a'))
str_b=list(input('輸入字串b'))
for i in range(len(str_a)):
    if str_a[i] in str_b and str_a[i] not in com:
        com.append(str_a[i])
if com==[]:
    print('N')
else:
    print(com)            