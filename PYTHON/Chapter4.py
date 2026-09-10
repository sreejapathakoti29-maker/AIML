# List and tuple
# 1. list fruits entered by user

fruits = []
f1="banana" or input("Enter Fruit name : ")
fruits.append(f1)
f2="banana" or input("Enter Fruit name : ")
fruits.append(f2)
f3="banana" or input("Enter Fruit name : ")
fruits.append(f3)

print(fruits)

# 2. marks list of students then display in sorted order
# marks=[]
# for i in range(0,6):
#     m=int(input("Enter marks : "))
#     marks.append(m)
# print(marks)
# marks.sort()
# print(marks)

# 3.type cannot be changed in python
t1=(1,2,"abc","xyz")
#t1[1]="sjhg" # gives error

# 4. sum a list
l2=[1,2,3,4,5]
print(sum(l2))

# 5. count number of zeros
l3=[0,0,9,0,80]
ans=l3.count(0)
print(ans)