def associative_add(a,b,c):
    lhs= a+(b+c)
    rhs= (a+b)+c
    return lhs== rhs
def associative_mul(a,b,c):
    lhs=a*(b*c)
    rhs=(a*b)*c
    return lhs==rhs
a=int(input("Enter a :"))
b=int(input("Enter b :"))
c=int(input("Enter c :"))
addition=associative_add(a,b,c)
multiplication=associative_mul(a,b,c)
print("Addition :",addition)
print("Multiplication :",multiplication)
