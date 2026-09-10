# Dictionary and Sets

# 1.create a dict of hindi words with values as english translation provide user with an option to look it up !
'''h_e={"kya":"What","billi":"cat","madad":"help"}
word=input("Enter the word to know its english version : ")
print(h_e[word])'''

# 2. input num from user and display all unique num only

num=set()
n=1 or input("Enter num1 : ")
num.add(int(n))
n=1 or input("Enter num2 : ")
num.add(int(n))
n=1 or input("Enter num3 : ")
num.add(int(n))
n=1 or input("Enter num4 : ")
num.add(int(n))
n=1 or input("Enter num5 : ")
num.add(int(n))
n=1 or input("Enter num6 : ")
num.add(int(n))
n=1 or input("Enter num7 : ")
num.add(int(n))
n=1 or input("Enter num8 : ")
num.add(int(n))
print(num)

# 3. set with 18 in and '18' str as a value in it ?
s={18}
s.add("18")
print(s)

# 4. wt is len of s1
s1=set()
s1.add(20)
s1.add(20.0)
s1.add("20")
print(s1)
print(len(s1))

# 5. typr of s3={}
s3={}
print(type(s3))

# 6. empty dict allow 4 frnds to enter their fav lang as value and use their names as key 
'''fav_lang={}
for i in range(0,5):
    key=input("Enter ur name : ")
    value=input("Ur fav lang : ")
    fav_lang.update({key:value}) # or fav_lang[key]=value
print(fav_lang)'''

# 7. if names of 2 frnds same in 6 
# 8. if lang of 2 frnds same then what
# 9. can u change the values inside a list which is ccontained in set s5
s5={8,7,12,"Harry",[1,2]}
# list not allowed in set
print(s5)