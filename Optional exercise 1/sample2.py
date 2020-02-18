slist=["AS","TO","thug","life"]
for i in slist:
    print(i)
slist.append("ok doing")
slist.insert(2,"leg")    
slist.sort()
print(slist)
print(slist[1])
for i in range(len(slist)):
    print(slist[i])

pain=[1,2,3,5,45,34,4,4,2,2]
print(pain.count(4))
pain.sort()
pain.reverse() 
print(pain)

def FizBuzzz(u): 
        for i in range(u):
            if ((i+1)%9==0 and (i+1)%7==0):
                print(str(i+1)+" Fizz Bizz")
            else:        
                if ((i+1)%7==0):
                    print(i+1,"IM Fizz")
                elif((i+1)%9==0):
                    print(i+1,"Im Bizz")            
                else:
                        print(str(i+1)+"Safe")           

print(FizBuzzz(130))