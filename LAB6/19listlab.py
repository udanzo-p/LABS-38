len=int(input("Enter N"))
len2=int(input("Enter N2"))
list1=[] 
for i in range(0, len): 
    ele = int(input()) 
    list1.append(ele)
print("for list 2")
list2=[]
for i in range(0, len2): 
    ele = int(input()) 
    list2.append(ele)

print(list(set(list1) - set(list2)))
