hour_1,min_1,sec_1=map(str,input('輸入時間1').split(":"))
time=int(input('輸入時間2：'))
ans1=int(hour_1)*3600+int(min_1)*60+int(sec_1)
hour_2=time//3600
min_2=time%3600//60
sec_2=time%3600%60
print('時間1 ('+hour_1+':'+min_1+':'+sec_1+")轉換格式後為"+str(ans1)+'秒')
print('時間2('+str(time)+'秒)='+str(hour_2)+':'+str(min_2)+':'+str(sec_2))