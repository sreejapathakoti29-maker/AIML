# Q1: Write a program to find the greatest of four numbers entered by the user.

# Q2: Write a program to check whether a student has passed or failed.
#     Passing criteria: total >= 40% AND at least 33% in each subject.
#     Assume 3 subjects and take marks as input.

# Q3: A spam comment is defined as text containing any of these keywords:
#     "Make a lot of money", "buy now", "subscribe this", "click this".
#     Write a program to detect spam.

# Q4: Write a program to check whether a given username contains less than 10 characters.

# Q5: Write a program to check whether a given name is present in a list.

# Q6: Write a program to calculate the grade of a student based on marks:
#     90–100 => Ex
#     80–90  => A
#     70–80  => B
#     60–70  => C
#     50–60  => D
#     <50    => F

# Q7: Write a program to check whether a given post is talking about "Harry" or not.
#1
# max=0
# for i in range(1,5):
#  num=int(input("enter the number:"))
#  if(num>max):
#   max=num
# print(max)
#2
# total=0
# marks1=int(input("entter marks 1: "))
# marks2=int(input("entter marks 2: "))
# marks3=int(input("entter marks 3: "))
# total=(marks1+marks2+marks3)/3
# if(total>=40 and marks1>=33 and marks2>=33 and marks3>=33):
#     print("passed")
# else:
#     print("fail")
#3
# p1= "Make a lot of money"
# p2="buy now"
# p3="subscribe this"
# p4="click this"
# msg=input("enter the msg:")
# if(p1 in msg or p2 in msg or p3 in msg or p4 in msg):
#     print("this content is spam")
# else:
#     print("this conetent is not spam")
#4
# string=input("enter the string")
# if(len(string)<10):
#     print("chars are less than 10")
# else:
#     print("sreeja is good")
#5
# list=["sreeja","hasini","preetham","sanni","ruthvika"]
# name=input("enter the name: ")
# if(name in list):
#     print("your name is in the list")
# else:
#     print("hasini loves ram")
#6
# marks=int(input("enter the marks="))
# if(marks>=90):
#     print("EX")
# elif(marks>=80):
#     print("A")
# elif(marks>=70):
#     print("B")
# elif(marks>=60):
#     print("C")
# elif(marks>=50):
#     print("D")
# else:
#     print("fail")
#7
post="harry is an excellent python teacher"
if("harry"in post):
    print("the post is talking about harry")
else:
    print("no")

