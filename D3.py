'''class Bank:
    bname="IDFC"
    branch="madurai"
    IFSC="IBO-09876543"
    def __init__(self,name,ph):
        self.n=name
        self.p=ph
    def disp(self):
        print(f"{self.n} \n{self.p}")
obj=Bank("TITAN",12345678)
obj.disp()
#obj.name="TITAN"
#obj.ph=1234567890
'''    

class Bank:
    bname="IDFC"
    branch="madurai"
    IFSC="IBO-09876543"
    def __init__(self,name,ph,address,amt=5000):
        self.name=name
        self.ph=ph
        self.address=address
        self.amt=amt

    def disp(self):
        print(self.name,self.ph,self.address,self.amt) # obj methods

    def ch_add(self,new):
        self.address=new
    def ch_ph(self,new):
        self.ph=new

    @classmethod
    def display(c):
        print(c.bname,c.branch,c.IFSC) #Here we have used the variable name as c.But we use the variable self and cls for industrial standards
    
    @classmethod
    def ch_bname(cls,new):
        cls.bname=new
    
    #def disp(self):
    #    print(self.name,self.ph,self.address,self.amt) # obj methods

    #def ch_add(self,new):
    #    self.address=new
    #def ch_ph(self,new):
    #    self.ph=new
    
    @staticmethod
    def add(a,b):
        return a+b
    def depo(self,i_amt): #this i_amt contains the initial amount 5000  of c1
        if(i_amt>=25000):
            print("Limit excedded") #we update the amount from the Bank to change the default amount 5000
        else:
            #self.amt=Bank.add(self.amt,i_amt)
            self.amt=Bank.add(self.amt,i_amt)

    @staticmethod
    def sub(a,b):
        return a-b
    def withdraw(self,i_amt):
        if(self.amt>=i_amt):
            self.amt=Bank.sub(self.amt,i_amt)
        else:
            print("Insufficient balance")

c1=Bank("PAL",1234569,'tokyo')
c1.ch_add("london")
c1.disp()

c2=Bank("MAX",1234569,'dubai',amt=20000)
c2.ch_ph(69696969)
c2.disp()

Bank.disp(c1)  #accessing obj methods through the class

Bank.ch_bname("IDBI") #changing the bname using new name
Bank.display()

c1.withdraw(0)
#c1.disp()
c1.depo(12000)
c1.disp()