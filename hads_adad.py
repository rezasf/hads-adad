# Copyright (C) 2021 rezasf - All Rights Reserved
import random
res = random.randint(0,40)
count = 1

while True:
    daf =int(input("ye adad vared kon:  "))
    if daf == res :
        print("bad az "+ str(count) +" bar talash"+" shoma bordid")
        break
    elif daf > res :
        print("bro pain") 
        count += 1
    elif daf < res :
        print("bro bala") 
        count += 1 
