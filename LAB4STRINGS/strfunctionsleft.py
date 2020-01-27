str="Left some string @%##@#&* functions"
var1="4 instance Ill finish this today"
var2="123456789"
var3="098765432"
dict={"a":"z","b":"y","c":"x","9":"1"}
print(str.find("s"))#prints 1st index of char found
print(var1.find("I",0,10))
print(var1.find("i",0,len(var1)))#searches between index no.
print(str.expandtabs())
print(var1.expandtabs(10))
print(str.ljust(40,"!"))#Adds extra character to string length to whatever was given ex 40
print(var1.ljust(3,"q"))#prints only string since less space provided
print(str.encode())
#print(str.decode(encoding='UTF-8',errors='strict'))
print(var2.maketrans(var2,var3))#for 1 dictionary or for more equal length
print(str.maketrans(dict))#some sort of ascii characters
print(str.rfind("@",0,len(var1)))#search backward but tried to do ind diff index
print(str.rindex("@",0,len(str)))#almost same otput in prev 2
print(str.count("s",0,len(str)))
print(var1.splitlines(len(var2)))
print(var3.split("0",12))
print(var2.translate(dict))
print(var1.rjust(35))#adjust white space in front if length more than string
