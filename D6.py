#'''#Access specifier program
class Mobile_phone:
    def __init__(self,brand,battery,pin):
        self.brand=brand
        self._battery=battery
        self.__pin=pin
        
    def show_brand(self):
        return f"Brand of mobile phone is {self.brand}"
    def show_battery(self):
        return f"Battery is {self._battery}" # protected can be accessed just like private just like it is declared.
    def get_pin(self):
        return f"secret pin is {self.__pin}" #to access the private var i can use syntax method or i can use get and set method
    def set_pin(self,new):
        self.__pin=new
        return ('Pin updated sucessfully')
m1=Mobile_phone("ROG","6000mah",4444)
#print(m1.show_brand())
#print(m1.show_battery())
#print(m1.get_pin())
print(m1.brand)
print(m1._battery) # I am accessing a protected var outside the class like a public. This is how protected work
print(m1.get_pin())# method to get the pin
print(m1.set_pin("7777"))# this is the function we wrote to change the private var.
print(m1.get_pin())#we have modified the private variable.
#'''
'''
# ----Abstarction-----
#points to remenber before using abstarction:
#1. from abc import ABC,abstractmenthod
from abc import ABC,abstractmenthod #we need to use to before using abstaction concept in our program
class A(ABC):            #for abstract class i can't create an object
    @abstractmenthod #decorator: it adds additional task without changing its original function
    def mname(args): 
        pass
class Cname1(A):
    def mname(args):
         #statement Block
         pass
obj=Cname1()
obj.mname()
#This is an outline of Abstraction program.
'''
'''
#Example code for Abstraction:-
from abc import ABC,abstractmethod                         
class Car(ABC): #we are importhing ABC object here.
    @abstractmethod #This is a decorator which we wirte when we define a abstract method.
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
#we will write only the pass in The statement block of the abstract 
class Petrol_car(Car):
    def start(self):
        return("Petrol car starts with vroom vroom")
    def stop(self):
        return("car stops")
class Electric_car(Car):
    def start(self):
        return("Electric car starts silently")
    def stop(self):
        return("Electric car stops")
p=Petrol_car()
e=Electric_car()
print(p.start())
#'''
'''#Abstract method program
from abc import ABC,abstractmethod
class Calc(ABC):
    @abstractmethod
    def add(a,b):
        pass
    @abstractmethod
    def sub(a,b):
        pass
    @abstractmethod
    def mul(a,b):
        pass
class Calc_upd(Calc):
    @staticmethod
    def add(a,b):
        print(a+b)
    @staticmethod
    def sub(a,b):
        print(a-b)
    @staticmethod
    def mul(a,b):
        print(a*b)
obj=Calc_upd()
obj.add(3,4)
'''
'''#abstract method program
from abc import ABC,abstractmethod
class Remote(ABC):
    @abstractmethod
    def change_vol(self):
        pass
    @abstractmethod
    def change_channel(self):
        pass
class Control(Remote):
    @staticmethod
    def change_vol(self):
        print("Volume changes")
    @staticmethod
    def change_channel(self):
        print("Channel changes")
obj=Control()
Control.change_channel(obj)
'''