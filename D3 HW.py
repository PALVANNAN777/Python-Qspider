class College:
    cname='Panimalar'
    loc='Chennai'
    area='600123'
    def __init__(self,name,regno,dept,cgpa=0):
        self.name=name
        self.regno=regno
        self.dept=dept
        self.cgpa=cgpa
    
    def disp(self):
        print(self.name,self.regno,self.dept,self.cgpa)

    def ch_dept(self,new):
        self.dept=new
    
    @classmethod
    def disp1(cls):
        print(cls.cname,cls.loc,cls.area)

    @classmethod
    def ch_loc(cls,new):
        cls.loc=new


    @staticmethod     # static method is an helper function which can by used to add external functionality to the exiting functions.       
    def cgpa_check(cgpa): #I have directly passed the variable without using the self key. 
        if 0<=cgpa and cgpa<=10:
            return f"{cgpa} is valid"
        else:
            return f"{cgpa} is invalid"
    #def check(self,check_cgpa):
        #if check_cgpa==True:
            #print(f"{self.cgpa} is valid")
        #else:
            #print(f"{self.cgpa} is invalid")


    def grade(self):
        if(self.cgpa>=7 and self.cgpa<8):
            print("Good")
        elif(self.cgpa>=8 and self.cgpa<9):
            print("Awesome")
        elif(self.cgpa>=9 and self.cgpa<10):
            print("Excellent")
        else:
            print("You have a less CGPA")
    
College.disp1() #Access class methods

s1=College("pal","850","cse",8.8)
College.disp(s1) #Sample obj method

s1.ch_dept("AIML") #ch_dept() is a normal method so i need to call it with object.
s1.disp()  #obj method changeing

College.ch_loc("!Chennai")
College.disp1() #class method changing

print(College.cgpa_check(8.8)) #passed directly to the static method

#College.grade(s1) #Normal method 
s1.grade()