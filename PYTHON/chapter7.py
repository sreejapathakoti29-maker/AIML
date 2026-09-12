# Q1: Write a program to print the multiplication table of a given number using a for loop.

# Q2: Write a program to greet all the person names stored in a list 'l' that start with 'S'.
#     Example list: l = ["Harry", "Soham", "Sachin", "Rahul"]

# Q3: Attempt Problem 1 using a while loop.

# Q4: Write a program to check whether a given number is prime or not.

# Q5: Write a program to find the sum of the first n natural numbers using a while loop.

# Q6: Write a program to calculate the factorial of a given number using a for loop.

# Q7: Write a program to print the following star pattern for n = 3:
#     *
#     ***
#     *****

# Q8: Write a program to print the following star pattern for n = 3:
#     *
#     **
#     ***

# Q9: Write a program to print the following star pattern for n = 3:
#     * * *
#     * *
#     * * *

# Q10: Write a program to print the multiplication table of n using for loops in reversed order.

# #1
# num=int(input("enter the number"))
# for i in range(1,11):
#     print(f"{num}*{i}={num*i}")
#2
# l = ["Harry", "Soham", "Sachin", "Rahul","Sreeja"]
# for i in l:
#     if(i.startswith('S')):
#         print("hello")
#3
# num=int(input("enter the number"))
# i=1
# while(i<=10):
#      print(f"{num}*{i}={num*i}")
#      i=i+1
# #4
# num=int(input("enter the number"))
# count=0
# for i in range(1,num+1):
#     if(num%i==0):
#         count=count+1
# if(i==1):
#     print("neither prime nor composite")
# elif(count==2):
#     print("prime")
# else:
#     print("not prime")
#5
# n=int(input("enter the number"))
# i=0
# while(i<=n):
#     sum=(n*(n+1))/2
#     i=i+1
# print(sum)
# #6
# n=int(input("enter the number"))
# for i in range(1,n):
#     n=n*i
# print(n)
#7
# i=1
# n=int(input("enter the no.of rows"))
# for i in range(n):
#     print('*'*((2*i)+1))
#8
# i=1
# n=int(input("enter the no.of rows"))
# for i in range(n+1):
#      print('*'*i)
#9
i=1
# n=int(input("enter the no.of rows"))
# for i in range(n):
#      if(i==1):
#        print('*'*(n-1))
#      else:
#       print('*'*n)
# #10
# num=int(input("enter the num"))
# for i in range(10,0,-1):
#      print(f"{num}*{i}={num*i}")
#11
# n=int(input("enter the number"))
# for j in range(n):
#      print(" "*(n-j-1),end="")
#      print('*'*((2*j)+1))
#12
i=0
n=int(input("enter the no.of rows"))
for i in range(n):
   if(i==1):
     print('*',end="")
     print(' ',end="")
     print('*')
   else:
    print('*'*n)










