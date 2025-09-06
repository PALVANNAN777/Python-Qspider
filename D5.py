#'''#Hybrid inheritance.........
class Upper:
    @staticmethod #it will give all the upper case
    def upp():
        out=' '
        for i in range(ord('A'),ord('Z')+1): #ord(' Z ')+1 this is used to include Z in the range.
            out+=chr(i)
        print(out)
Upper.upp()

class Alphabets(Upper):
    @staticmethod
    def low():
        out=' '
        for i in range(ord('a'),ord('z')+1): #ord(' z ')+1 this is used to include Z in the range.
            out+=chr(i)
        print(out)

class Digit():
    @staticmethod
    def num():
        out=''
        for i in range(0,10):
            out+=str(i)
        print(out)

class Character(Alphabets,Digit):
    sc='!@#$%^&*()'

ob=Character()
Character.low()
ob.num()
#'''


'''#polymorphism....
#The two types of polymorphism.
#1.Method and 2.operator overloading.
def sam():
    print("Hello")
mid=sam #Now the variable mid stores the addres of sam(), Therefore when i want this method i call mid insted of sam.This is called as Monkey patching.
def sam(a,b):
    print(a+b)
add=sam
def sam(a,b,c):
    print(a+b+c)
a3=sam
#print(sam)
mid() #over loading
add(5,5)
a3(1,2,3)
'''
'''
#operator overolading Assignment...
class A:
    def __init__(self,a):
        self.a=a
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

ob1=A(10)
ob2=A(5)
print(ob1+ob2)
print(ob1-ob2)
print(ob1*ob2)
print(ob1/ob2)
print(ob1//ob2)

#print(dir(str))
'''
'''
#Encapsulation.......
#public
class A:
    x=10 # x is a public class variable
    def __init__(self,m):
        self.m=m # m is a public instance variable
o1=A(123) # as m is declared in the instance variable we need to pass some in value.
print(o1.x)# this show the x is a plublic 

#protected
class A:
    _x=10 # x is a protected class variable 
    def __init__(self,m):
        self.m=m
o1=A(123)
print(o1._x) # x is a protected variable 
'''
'''
class Company:
    cname='Qspiders'
    CEO='Mark'
    __noemp=100 #private
    loc='Banglore'

    def __init__(self,tname,tid,phone,email,sal):
        self.tname=tname
        self.tid=tid
        self.__phone=phone #private members
        self.email=email
        self.__sal=sal #private members
    
    def display(self):
        print(self.tname,self.email,self.tid)
    def ch_sal(self,new):
        self.sal=new
    @classmethod
    def disp(cls):                                                           
        print(cls.cname,cls.CEO,cls.loc)

t1=Company('sam',3181,987654311,"titan@gmail.com",50000)    
t1.display()
'''

'''
 #getter and setter methods are not compulsory we write it  to access the private members in the industial standards

class Cname:
    def __init__(self,var):
        self.__var=var

    def get_var(self):
        return self.__var
    
    #def set_var(self,new):
        #self.__var=new

obj=Cname(50)                     
print(obj.get_var())                                       
#obj.set_var(34)

#here we dont use the set_var method but dont remove it because it can be developed to set our value.
'''
