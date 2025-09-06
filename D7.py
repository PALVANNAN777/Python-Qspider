#operator overolading Assignment...
class A:
    def __init__(self,a):
        self.a=a
    #arithmetic operation
    def __add__(self,other):
        return self.a+other.a
    def __sub__(self,other):
        return self.a-other.a            
    def __mul__(self,other):
        return self.a*other.a
    def __truediv__(self,other):
        return self.a/other.a
    def __floordiv__(self,other):
        return self.a//other.a
    def __mod__(self,other): 
        return self.a%other.a
    def __pow__(self,other): 
        return self.a**other.a
    #comparision operation
    def __eq__(self,other):
        return self.a == other.a
    def __ne__(self, other):
        return self.a != other.a
    def __lt__(self,other):
        return self.a < other.a
    def __gt__(self,other):
        return self.a > other.a
    def __le__(self,other):
        return self.a <= other.a
    def __ge__(self,other):
        return self.a >= other.a
    # Bitwise operation
    def __and__(self,other): 
        return self.a & other.a
    def __or__(self,other): 
        return self.a | other.a
    def __xor__(self,other): 
        return self.a ^ other.a
    def __lshift__(self,other): 
        return self.a << other.a
    def __rshift__(self,other): 
        return self.a >> other.a
    def __invert__(self): 
        return ~self.a
    # Unary operation
    def __neg__(self): 
        return -self.a
    def __pos__(self): 
        return +self.a
    def __abs__(self): 
        return abs(self.a)


# Example test
ob1=A(10)
ob2=A(5)

print(ob1+ob2)
print(ob1-ob2)
print(ob1*ob2)
print(ob1/ob2)
print(ob1//ob2)
print(ob1%ob2)
print(ob1**ob2)

print(ob1==ob2)
print(ob1!=ob2)
print(ob1<ob2)
print(ob1>ob2)
print(ob1<=ob2)
print(ob1>=ob2)

print(ob1&ob2)
print(ob1|ob2)
print(ob1^ob2)
print(ob1<<ob2)
print(ob1>>ob2)
print(~ob1)

print(-ob1)
print(+ob1)
print(abs(ob1))


#print(dir(str))

'''
#This code is used to see all magic method of a particular data type.
print(dir(int))
'''
# Data types
