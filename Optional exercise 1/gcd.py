print("Enter no.s  to find GCD")
var1=int(input())
var2=int(input())
def GCD(a,b):
    if (b>a):
        return GCD(b,a)
    if(b==0):
        return a
    else:
        return GCD(b,a%b)
z=GCD(var1,var2)
print("The gcd is ",z)
