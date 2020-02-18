'''import sys
import datetime
import math
print("Question 2")
print("Python Version is")
print(sys.version)
print("Version info.")
print (sys.version_info)
print("Question 3")
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
print("Question 5")
str=input()
str1=input()
print(str[::-1]+" ",str1[::-1])
'''
print("Question 7")
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))

filename=input('Enter a filename: ')
index=0
for i in range(len(filename)):
    if filename[i]=='.':
       index=i
print(filename[index+1: ])
    