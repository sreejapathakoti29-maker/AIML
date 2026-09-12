'''
snake=1
water=-1
gun=0
'''
import random
computer=random.choice(['snake','water','gun'])
you=input("enter your choice")
print(f"my choice is:{you}")
print(f"compter choice is:{computer}")
if(computer==you):
    print("draw")
else:
    if(computer=='snake' and you=='water'):
        print("you LOST,computer WON")
    elif(computer=='snake' and you=='gun'):
        print("you WON ,computer LOST")
    elif(computer=='gun' and you=='water'):
        print("you WON ,computer LOST") 
    elif(computer=='gun' and you=='snake'):
        print("you LOST,computer WON")
    elif(computer=='water' and you=='gun'):
        print("you LOST ,computer WON")
    elif(computer=='water' and you=='snake'):
        print("you WON ,computer LOST")
    else:
        print("something is invalid!!!")