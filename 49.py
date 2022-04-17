str=[]
sentence=list(input('輸入英文句子').split())
for i in range(len(sentence)-1,-1,-1):
    str.append(sentence[i])
print("輸出結果為",str)