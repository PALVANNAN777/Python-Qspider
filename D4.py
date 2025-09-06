'''#multilevel inheritance...

class Res10:               #parent class
    rname="10th resume"
    def __init__(self,name,dob,phone,tp,tyop):
        self.name=name
        self.dob=dob
        self.phone=phone
        self.tp=tp
        self.tyop=tyop
    def display(self):
        print(self.name,self.dob,self.phone,self.tp,self.tyop)
o1=Res10("Pal","10-06-2006",987654567,88,2021)
o1.display()

class Res12(Res10):
    rname="12th Resume"
    def __init__(self,name,dob,phone,tp,tyop,interp,interyop):
        super().__init__(name,dob,phone,tp,tyop) 
        self.interp=interp 
        self.interyop=interyop

    def display(self):
        print("----RESUME----")
        super().display()
        print(self.interp,self.interyop)

class ResBE(Res12):
    def __init__(self,name,dob,phone,tp,tyop,interp,interyop,BEp,BEyop): #Note: Year of BE passout -> BEypop and BE pass percentage is BEp
        super().__init__(name,dob,phone,tp,tyop,interp,interyop)
        self.BEp=BEp
        self.BEyop=BEyop
    def display(self):
        super().display()
        print(self.BEp,self.BEyop)

oBE=ResBE('PALVANNAN','16/06/2006',987654567,88,2021,88.7,2023,8.8,2024)
oBE.display()
'''

'''#Multiple inheritance

class Addition:
    def add(self,a,b):
        print("Addition is ",a+b)
        
class Subtraction:
    def sub(self,a,b):
        print("Addition is ",a-b)

class Multiplication:
    def mul(self,a,b):
        print("Addition is ",a*b)
        
class Division:
    def div(self,a,b):
        print("Addition is ",a/b)

class Calc(Addition,Subtraction,Multiplication,Division):
    def __init__(self):
        self.a=int(input("Enter the number 1:"))
        self.b=int(input("Enter the number 2:"))
        print("Enter 1 for Addition ")
        print("Enter 2 for Subtraction ")
        print("Enter 3 for Multiplication ")
        print("Enter 4 for Division ")

        ch=int(input("Enter choice: "))
        if ch==1:
            self.add(self.a,self.b)
        elif(ch==2):
            self.sub(self.a,self.b)
        elif(ch==3):
            self.mul(self.a,self.b)
        elif(ch==4):
            self.div(self.a,self.b)
        else:
            print("ERROR!!!  Invalid Choice")
obj=Calc()
'''
'''
#Hierarchicial Inheritance......

class Social_media:
    def __init__(self,usrname,pd,post,following,followers):
        self.usrname=usrname
        self.pd=pd
        self.post=post
        self.following=following
        self.followers=followers
    def display(self):
        print(self.usrname,self.pd,self.post,self.following,self.followers)
    def login(self,un,psd):
        if un==self.usrname:
            if psd==self.pd:
                print("Login Successful!!!")
            else:
                print("Incorrect password :(")
        else:
            print("Invalid Credentials")

    def add_post(self):
        self.post+=1

    def remove_post(self):
        self.post-=1

    def add_follower(self):
        self.followers+=1

    def remove_follower(self):
        self.followers-=1

    def add_following(self):
        self.following+=1

    def remove_following(self):
        self.following-=1

class Insta(Social_media):
    pass

class FB(Social_media):
    pass

obj1=FB('Panimalar',1234,1,0,0)
obj1.display()
obj2=Insta('TITAN',123456,100,200,300)
obj2.display()
obj2.add_follower()
obj2.display()
obj1.login("Panimalar",1234)

'''


'''
#Today's HOME WORK.....................

#Creating single inheritance..
class A:
    def __init__(self,cname,ctype):
        self.cname=cname
        self.ctype=ctype
    def display(self):
        print(self.cname,self.ctype)
obj=A("panimalar","friendly") #I send the values to the class by declaring an object 
obj.display() # now we are accessing the method in side the class which has the print func. to diplay the values
class B(A):
    def __init__(self, cname, ctype,sname,stype):
        super().__init__(cname, ctype)
        self.sname=sname
        self.stype=stype
    def display(self):
        super().display()
        print(f"{self.sname} {self.stype}")
obj1=B("Panimalar","Redemption","Palvannan","Idiot")
obj1.display()
'''
'''
#Multilevel Inheritance
class Person:                               #Grand Parent
    def __init__(self,name):
        self.name=name
    def disp_name(self):
        print(self.name)
obj=Person("palvannan")
obj.disp_name()

class Student(Person):                     #Parent
    def __init__(self,name,std_id):
        super().__init__(name)
        self.std_id=std_id
    def disp_std(self):
        super().disp_name() 
        print(self.std_id)
obj1=Student("PAL",850)
obj1.disp_std()

class Graduate(Student):                 #children
    def __init__(self, name, std_id,degree):
        super().__init__(name, std_id)
        self.degree=degree
    def disp_graduate(self):
        super().disp_std()
        print(self.degree)
obj2=Graduate("PALVANNAN",850,"BE-CSE")
obj2.disp_graduate()
'''

# Multiple inheritance
class Teacher:
    def __init__(self,subject):
        self.subject=subject
    def teach_subject(self):
        print(f"Teacher teaches:{self.subject}")

class Researcher:
    def __init__(self,research):
        self.research=research
    def do_research(self):
        print(f"Researcher researches:{self.research}")

class Professor(Teacher,Researcher):
    def __init__(self, subject,research,teaches):       
        Teacher.__init__(self,subject)      #parent.__init__(self,args) we use this syntax here,   
        Researcher.__init__(self,research)     #because "super().__init__(args)" this syntax will cause confusion because of 2 "super().__init__(args)"  
        self.teaches=teaches
    def guide_students(self):
        self.teach_subject()              #changed Teacher.teach_subject() to self.teach_subject()
        self.do_research()                #changed Reacher.do_research() to self.do_research()
        print(f"Professer lectures: {self.teaches}")

obj=Professor("Python","Nano-tech","tech-development")
obj.guide_students()


'''
# Vechicle Modification an example for Hierarchical Inheritance
class Vehicle:
    def __init__(self,engine):
        self.engine=engine
    def start_engine(self):
        print(f"Engine type: {self.engine}")

class Car(Vehicle):
    def __init__(self,engine,type):
        super().__init__(engine)
        self.type=type
    def car_type(self):
        super().start_engine()
        print(f"Engine type:{self.engine} Hybrid/Combustion/electric:{self.type}")

class Bike(Vehicle):
    def __init__(self,engine,start_tp):
        super().__init__(engine)
        self.start_tp=start_tp
    def kick_start(self):
        super().start_engine()
        print(f"Engine type:{self.engine} Starting:{self.start_tp}")

class Bus(Vehicle):
    def __init__(self,engine,AC):
        super().__init__(engine)
        self.AC=AC
    def open_door(self):
        super().start_engine()
        print(f"Engine type:{self.engine} AC or NON-AC:{self.AC}")

obj=Car("V12","Hybrid")
obj.car_type()
'''

#3 syntax for Constructor chaining
# 1) super().__init__(args)
# 2) super(child,self).__init(args)
# 3) parent.__init__(self,args)
'''
class Teacher:
    def __init__(self,subject):
        self.subject=subject
    def teachsubject(self):
        print(self.subject)

class Reacher:
    def __init__(self,research):
        self.research=research
    def doresearch(self):
        print(self.research)

class Professor(Teacher,Reacher):
    def __init__(self, subject,research,teaches):       
        Teacher.__init__(self,subject)      #use of two super(),controller confuses which parent 
                                            #so takes Teacher by default so instead of super() syntax use: parent.__init__(self,args)
        Reacher.__init__(self,research)
        self.teaches=teaches
    def guide_students(self):
        super().teachsubject()
        super().doresearch()
        print(self.teaches)

obj=Professor("Python","Nano-tech","tech-development")
obj.guide_students()'''