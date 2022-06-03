dict1= {'蘋果': 'red', '香蕉': 'yellow','葡萄':'purple',"橘子":'orange','藍莓':'blue'}
str=input("輸入水果名稱：")
if str in dict1:
    print(str+'是'+dict1.get(str))
else:
    print('不存在字典當中')    