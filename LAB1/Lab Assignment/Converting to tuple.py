List = []
#initializing empty list
num=int(input("Enter the no. of elements to be present in list\t"))
# To add elements using append which is inbuilt
for i in range(0, num):
    print("Enter data:")
    item = int(input())
    List.append(item)
tup=tuple(List)
print("The new datatype is",tup)