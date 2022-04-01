from __future__ import print_function
from tabnanny import check


while True:
    voc=input("檢測字元")
    list1=list(voc)
    if voc=='end':
        print("end")
        break
    check=input("檢測單一字元")
    if check in list1:
        answer=list1.count(check)
        print("字元"+check+"出現次數為:"+str(answer))