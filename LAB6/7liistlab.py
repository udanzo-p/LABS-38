#Remove duplicate in list
len=int(input("Enter N"))
list1=[] 
for i in range(0, len): 
    ele = int(input()) 
    list1.append(ele)
list=set(list1)
print(list)