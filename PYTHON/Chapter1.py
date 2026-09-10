# twinkle twinkle poem

'''print("""Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky""")'''

# 3.
'''
import pyttsx3
engine = pyttsx3.init()

# engine.say("I will speak this text")
engine.say("Hey hasini")

engine.runAndWait()'''

#4
import os

#specify the directory you waant to list
directory_path ='/MINNU Album'

#List all files and directories in specified path
contents=os.listdir(directory_path)

#print each file and directory name
for item in contents:
    print(item)