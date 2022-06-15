id=['123','456','789','321','654']
name=['Tom','Cat','Nana','Lim','Won']
series=['DTGD','CSIE','ASIE','DBA','FDD']
que=input('輸入查詢學號為：')
ans=id.index(que)
print('學生資料為：'+que+' '+name[ans]+' '+series[ans])