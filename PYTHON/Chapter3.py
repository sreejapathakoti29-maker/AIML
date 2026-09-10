# 1. wish the user (entered by input)

name = "Sini" or input("Enter ur name : ")

print(f"Good mrng {name}")

# 2. 
letter = '''Dear <|Name|>,
you are selected!
<|Date|>'''
print(letter.replace("<|Name|>","Hasini").replace("<|Date|>","25 September"))

# 3. 
name = "Harry is  a good boy"
print(name.find("  ")) # returns index of the req specific occcurance

# 4.
print(name.replace("  "," "))

# 5. 
letter = "Dear 'Harry',\n\t this is python course is nice ,\n Thanks"
print(letter)

a=None
print(type(a))

s="Hello"
print(s)
a=s.replace("l","b")
print(a)

print("hey 'sreeja'")