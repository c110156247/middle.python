a,b=input('輸入遊戲時間：').split(":")
min=int(a)
sec=int(b)
game_time=min*60+sec
if game_time>=75:
    cs1_start_time=75
    cs_time=30
    cs_eat_time=game_time-cs1_start_time
    csb=cs_eat_time//30+1
    cs_num=csb*6
    cs_3b=(csb//3)
    cs_loss=csb//2
    cs_total=cs_num+cs_3b-cs_loss
    print(str(cs_total)+'隻兵')
else:
    print('吃屎囉')    