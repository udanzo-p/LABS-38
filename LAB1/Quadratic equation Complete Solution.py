import math
print("Enter the a,b,c of quadratic equation respectively")
a=int(input("a"))
b=int(input("b"))
c=int(input("c"))
sqrt=math.sqrt
pow=math.pow
disc=((pow(b,2))-4*a*c)
if(disc>0):
    disc=sqrt(disc)
    x=(-b+disc)/(2*a)
    y=(-b-disc)/(2*a)
    print("Roots are",x,y)
elif(disc==0):
    print("Roots are",(-b)/(2*a))
else:
    disc=sqrt(-disc)
    disc=complex(disc)
    x=(-b+disc)/(2*a)
    y=(-b-disc)/(2*a)
    print("Roots are",x,y)
