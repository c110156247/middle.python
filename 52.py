x1 = '紅豆生南國，春來發幾枝。願君多采擷，此物最相思。'
x2 = '春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少。'
ans = []
x = '，。'
for i in range(2):
    x1=x1.replace(x[i],"")
    x2=x2.replace(x[i],"")
for i in x1:
    for j in x2:
        if j == i:
            ans.append(j)
print(ans)