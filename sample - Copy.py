'''ch=input("Enter a character: ")
if(ch.isdigit()):
    print(f"{ch} is a digit ")
else:
    print(f"{ch} is not a digit ")'''

'''ch=input("Enter a character: ")
if(ch.isalnum()):
    print(f"{ch} is a Not special ")
else:
    print(f"{ch} is Special")'''

'''s=input("Enter a string:")
if s==s[::-1]:
    print(f"{s} is Palindrome")
else:
    print("Not a palindrome")'''

'''#prog to check the given data is mutable
def mutable(arr):
    if isinstance(arr, (set,list,dict)):
        return True
    else:
        return False
print("List: ",mutable([1,2,3]))
print("Dict: ",mutable({1:'a',2:'b',3:'c'}))
print("Tuple: ",mutable((1,2,3)))
print("String: ",mutable("TITAN"))'''

'''#prog to print all keywords in Python
import keyword
k=keyword.kwlist
print(k)'''

'''
#My example Prog for a constructor
#method 1- with function 
class Cat:
    def __init__(self,a,b):
        self.a= a
        self.b = b
        #print(f"{self.a}{self.b}")
    def display(self):
        print(f"{self.a}{self.b}")
n1=int(input("Enter N1: "))
n2=int(input("Enter N2: "))
obj=Cat(n1,n2)
obj.display()
'''

'''
#method 2-without a function
class Cat:
    def __init__(self,a,b):
        self.a= a
        self.b = b
        print(f"{self.a}{self.b}")
n1=int(input("Enter N1: "))
n2=int(input("Enter N2: "))
obj=Cat(n1,n2)
'''
'''
#Method 3-different parameter name
class Cat:
    def __init__(self,x,y):
        self.a= x
        self.b = y
        print(f"{self.a}{self.b}")
n1=int(input("Enter N1: "))
n2=int(input("Enter N2: "))
obj=Cat(n1,n2)
'''
'''n1=int(input("Enter a number: "))
if(n1%6==0 or n1%9==0):
    print("The cube of the number:",n1**3)
else:
    print("The number",n1,"is not divisible by 6 or 9")
'''

'''
str1 = input("Enter the string: ")
print(isinstance(str1,int))
'''

'''
s=input("Enter the string: ")
up=0;lr=0;dig=0;sl=0
for i in s:
    if(i.isupper()):
        up+=1
    elif(i.islower()):
        lr+=1
    elif(i.isdigit()):
        dig+=1
    else:
        sl+=1
print("The number of Uppercase in the string: ",up)
print("The number of Lowercase in the string: ",lr)
print("The number of Digit in the string: ",dig)
print("The number of Special in the string: ",sl)
'''

'''#insta login
n=input("Enter usr name: ")
if(n=='panimalar'):
    usr=int(input("Enter The password: "))
    if(usr==12345):
        print("Login successfull !!!")
    else:
        print("Invalid login!!")
else:
    print("Invalid user")
'''
'''
i=5
while(i>0):
    print("Python")
    i-=1
'''
'''
i=1
while(i<=10):
    print(i)
    i+=1
'''
'''
n=int(input("Enter the number:"))
count=len(str(n))
print(f"{count}")
if count==1:
    print("SIngle digit")
elif count==2:
    print("Double digit")
elif count==3:
    print("Tripple digit")
else:
    print("More than three digit")
'''
'''
n1=int(input("Enter the number 1: "))
n2=int(input("Enter the number 2: "))
if n1>n2:
    print(f"{n1} is greater than {n2}")
elif n1==n2:
    print(f"{n1} is equals to {n2}")
else:
    print(f"{n1} is Lesser than {n2}")
'''
'''
list=[10,20,"Thirty",40,50]

if len(list)%2!=0:
    mid=len(list)//2
    if isinstance(list[mid],str):
        print(list[mid])
    else:
        print("It is not a string")
else:
    print("No middle value")
'''
'''
n=int(input("Enter the number :"))
i=0
while(i<=10):
    print(n,"*",i,"=",n*i)
    i+=1
'''
'''
s=input("Enter the string: ")
result=[]
i=0
while(i<len(s)):
    if(s[i].islower()):
        result.append(s[i].upper())
    elif(s[i].isupper()):
        result.append(s[i].lower())
    else:
        result.append(s[i])
    i+=1
print("",result)    
'''
'''n=1
print(n%10)
print(n//10)
print(n/10)
'''
'''
n1=int(input("Enter the number: "))
rev=0
while(n1>0):
    dig=n1%10
    rev=rev*10+dig
    n1=n1//10
print(rev)
'''
'''n1=int(input("Enter the number: "))
add=0
while(n1>0):
    dig=n1%10
    add+=dig
    n1=n1//10
print(add)'''

'''
s=input(("Enter the string: "))
if(len(s)%2!=0):
    if s[0] in 'aeiouAEIOU':
        if s[-1]  not in 'aeiouAEIOU' and s[-1].isalpha():
            print(s[::-1])
        else:
            print("The last char is not constant")
    else:
        print("The first char is not vowel")
else:
    print("The characters are in even number")

'''
'''
s=['string',186,3.14]
i=0
for i in range(len(s)):
    if isinstance(s[i],int):
        print(s[i])
'''
'''
s=(123,2.17,"TITAN",1234)
count=0
for i in s:
    count += 1
print(count)
'''
'''
list=[1,2,3,4,5,6]
for i in range(len(list)):
    if list[i]%2==0:
        print(list[i])
'''
'''
list=[1,2,3,1,1,6,1]
list2=[]
for i in list:
    if i not in list2:
        list2.append(i)
print(list2)
'''
'''s=input("Enter a string")
rev=""
for i in range(len(s)-1,-1,-1):
    rev+=s[i]
print(rev)
'''
'''
s='power star'
word=s.split()
out={}
for i in word:
    out[i]=len(i)
print(out)
'''
'''
s='power star'
word=s.split()
out={}
for i in word:
    out[i]=i[::-1]
print(out)
'''
'''
s='power star'
word=s.split()
out={}
for i in word:
    count=0
    for p in i:
        count+=1
    out[i]=count
print(out)
'''
'''
s='power star'
word=s.split()
out={}
for i in word:
    count=0
    for p in i:
        if p in 'aeiou':
            count+=1
    out[i]=count
print(out)
'''
'''
def len():
    word=input("Enter a string: ")
    count=0
    for i in word:
        count+=1
    print(count)

len()
'''
'''
def neg():
    w=[1,2,-3,4,"sam",-7,10]
    for i in w:
        if isinstance(i,int) and i<0:
            print(i)
neg()'''

'''
def add( a,b):
    print("ADDITION:",a+b)
def sub( a,b):
    print("SUBTRACTION:",a-b)
def mul( a,b):
    print("MULTIPLICATION:",a*b)
def div( a,b):
    if a !=0:
        print("DIVITION:",a/b)
    else:
        print("Division Error")
def mod(a,b):
    if a !=0:
        print("MODULUS:",a%b)
    else:
        print("Division Error")

n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
print("1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n 5.Modulas\n")
ch=int(input("Enter your choice:"))
if ch == 1:
    add(n1,n2)
elif ch==2:
    sub(n1,n2)
elif ch==3:
    mul(n1,n2)
elif ch==4:
    div(n1,n2)
elif ch==5:
    mod(n1,n2)
else:
    print("Invalid choice")
'''
'''#prime number checking structure
def prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
print(prime(7))
'''
'''
#Example for static method
class MathTools:
    def __init__(self, x):
        self.x = x   # instance variable

    def square(self):   # normal method → uses self
        return self.x * self.x

    @staticmethod
    def add(a, b):   # static method → no self
        return a + b


# usage
#obj = MathTools(4)

#print(obj.square())      # 25 (uses self.x)
#print(obj.add(10, 20))   # 30 (doesn't care about self)
print(MathTools.add(7, 3))  # 10 (can even call with class name)
'''


