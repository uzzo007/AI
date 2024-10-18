def distributed_add(a,b,c):
    lhs=a*(b+c)
    rhs=a*b+a*c
    return lhs==rhs
def distributed_sub(a,b,c):
    lhs=a*(b-c)
    rhs=a*b-a*c
    return lhs==rhs
a=int(input("Enter a :"))
b=int(input("Enter b :"))
c=int(input("Enter c :"))
addition=distributed_add(a,b,c)
substraction=distributed_sub(a,b,c)
print("Addition :",addition)
print("Substraction :",substraction)
