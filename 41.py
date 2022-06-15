up=20
down=10
price=0
now_floor=1
user=int(input('搭了多少次電梯'))
for i in range(user):
    next_floor=int(input('到幾樓?'))
    if now_floor < next_floor:
        price+=(next_floor-now_floor)*up
        now_floor=next_floor
    elif now_floor > next_floor:
        price+=(now_floor-next_floor)*down
        now_floor=next_floor
print(str(price)+'元')            