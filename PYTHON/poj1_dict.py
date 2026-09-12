import random
computer=random.choice(['snake','water','gun'])
you=input("enter your choice")
print(f"my choice is:{you}")
print(f"compter choice is:{computer}")
value_dict={ "snake":1,"water":-1,"gun":0}
if(computer==you):
    print("draw")
else:
 sub=value_dict[computer]-value_dict[you]
 if(sub==-1 or sub==2):
    print("you lost ,computer win")
 else:
    print("you win,computer lost")