'''#operator overolading Assignment...
class A:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        return self.a+other.a
    def __sub__(self,other):
        return self.a-other.a            # Home work : complete this program for all the magic method for operation.
    def __mul__(self,other):
        return self.a*other.a
    def __truediv__(self,other):
        return self.a/other.a
    def __floordiv__(self,other):
        return self.a//other.a
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


ob1=A(10)
ob2=A(5)
print(ob1+ob2)
print(ob1-ob2)
print(ob1*ob2)
print(ob1/ob2)
print(ob1//ob2)
print(ob1==ob2)
print(ob1!=ob2)
print(ob1<ob2)
print(ob1>ob2)
print(ob1<=ob2)
print(ob1>=ob2)
'''


#print(dir(str))

'''
#This code is used to see all magic method of a particular data type.
print(dir(int))
'''
# Data typesk