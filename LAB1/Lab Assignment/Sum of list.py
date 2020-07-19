List = []
#initializing empty list
num=int(input("Enter the no. of elements to be present in list\t"))
# To add elements using append which is inbuilt
for i in range(0, num):
    print("Enter number at location", i, ":")
    item = int(input())
    List.append(item) 
sum=0 
#iterating through loop and adding element one by one
for i in range(num): 
    sum=sum+(List[i]) 
print("The sum of all elements in list is ",sum)
