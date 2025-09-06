class Bank:
    bname="IDFC"
    branch="madurai"
    IFSC="IBO-09876543"
    def __init__(self,name,ph,add,amt=5000):
        self.name=name
        self.ph=ph
        self.add=add
        self.amt=amt
    @classmethod
    def display(c):
        print(c.bname,c.branch,c.IFSC) #Here we have used the variable name as c.But we use the variable self and cls for industrial standards
    
    @classmethod
    def ch_bname(cls,new):
        cls.bname=new

    def disp(self):
        print(self.name,self.ph,self.add,self.amt) # obj methods
    def ch_add(self,new):
        self.add=new
    def ch_ph(self,new):
        self.ph=new

c1=Bank("PAL",1234569,'tokyo')
c1.ch_add("london")
c1.disp()
c2=Bank("MAX",1234569,'dubai',amt=20000)
c2.ch_ph(69696969)
c2.disp()
Bank.disp(c1)  #accessing obj methods through the class
Bank.ch_bname("IDBI") #changing the bname using new name
Bank.display()
