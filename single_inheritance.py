#This is a classmethod , objmethod & static method prog thought by sir on Day3
class Bank:
    bname='Indian Bank'
    loc='Chennai'
    IFSC='IB00XX57'

    def __init__(self,name,phno,addres,bal=500):
        self.name=name
        self.phno=phno
        self.addres=addres
        self.bal=bal

    @classmethod
    def display(cls):
        print(cls.bname,cls.loc,cls.IFSC)

    @classmethod
    def ch_loc(cls,new):
        cls.loc=new

    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def sub(a,b):
        return a-b

    def disp(self):
        print(self.name,self.addres,self.phno,self.bal)

    def ch_add(self,new):
        self.add=new

    def ch_phnno(self,new):
        self.phno=new    

    def deposit(self,amt):
        if 0<=amt>25000:
            print("Limit exceeded")
        else:
            self.bal=Bank.add(self.bal,amt)

    def withdrwal(self,amt):
        if self.bal>=amt:        
            self.bal=Bank.sub(self.bal,amt)
        else:
            print('insufficient balance')

c1=Bank('Jhonny',987654321,'Panimalar')
c2=Bank('Yogesh',86372201556,'banglore')
c3=Bank('Kriti',5678624862,'Kilpauk')


Bank.disp(c1)
Bank.display()
Bank.ch_loc('Goa')
Bank.display()
c1.deposit(1055550)
c1.withdrwal(400)
c1.disp()



#SINGLE LEVEL INHERITANCE ..............................

class Bank:
    bname='SBI'
    loc='panimalar'
    timing='Lunch break'

    def __init__(self,name,pin,phno,add,bal=0):
        self.name=name
        self.phno=phno
        self.add=add
        self.bal=bal
        self.pin=pin

class ATM(Bank):
    def check_bal(self):
        pn=int(input("Enter pin:"))
        if pn==self.pin:
            print(f"Available balance: {self.bal}")
        else:
            print("incorrect pin")

    def deposit(self):
        pn=int(input("Enter pin to deposite:"))
        if pn==self.pin:
            amt=int(input("Enter the amount you want to deposit: "))
            self.bal+=amt
            print(f"Amount {amt} deposited successfully")
        else:
            print("incorrect pin")

c1=ATM('Arjun',123,98765432,'Chennai')

c1.deposit()
c1.check_bal()