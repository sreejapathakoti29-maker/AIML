# # # Q1: Write a program using functions to find the greatest of three numbers.

# # # Q2: Write a Python program using a function to convert Celsius to Fahrenheit.

# # # Q3: How do you prevent a Python print() function from printing a new line at the end?

# # # Q4: Write a recursive function to calculate the sum of the first n natural numbers.

# # # Q5: Write a Python function to print the first n lines of the following pattern (for n = 3):
# # #     ***
# # #     **
# # #     *

# # # Q6: Write a Python function which converts inches to centimeters.

# # # Q7: Write a Python function to remove a given word from a list and strip it at the same time.

# # # Q8: Write a Python function to print the multiplication table of a given number.

# # #1
# # def greatest(a,b,c):
# #     if(a>=b and a>=c):
# #         print(f"{a} is max")
# #     elif(b>=a and b>=c):
# #         print(f"{b} is max")
# #     else:
# #         print(f"{c} is max")
# # greatest(8,4,9)
# #2
# # def convert(celcius):
# #     f=(9/5)*celcius+32
# #     return f
# # print(convert(30))
# #3
# #print("sreeja",end="")
# #4
# #def sum(n):
# #     if(n==0):
 #         return 
      ans=(n*(n+1))/2
     return ans
print(sum(5))
 #5
def pattern(n):
     for i in range(n):
        print('*'*(n-i))
pattern(3)
#6
def convert(n):
    c=n*2.54
    return c
print(convert(20))
#7
def remove(l,word):
   n=[]
   for item in l:
      if not(item==word):
         n.append(item.strip(word))
   return n
    
l=["sreejan","rohan","rajan","an"]
print(remove(l,"an"))    
#8
def mul(n):
    i=1
    for i in range(1,10):
        print(f"{n}*{i}=",n*i)
mul(10)