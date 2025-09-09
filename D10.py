
#Q1. Wap to get the following output.
#''' In=['hello',227,3.4,'last',189,34]
# Out=[722,981,43]'''

#Q2. Wap to get the following output.
#''' S=’power star’
# Out={‘power’:2,’star’:1}'''

#'''
#Q3. Wap to replace the special character present 
#    in a string by space.uuguyg8ihub

#'''
#Q4. Wap to extract all the mutable values present in a tuple
'''
#Q1:
ln=eval(input("Enter the collection: "))
out=[]
for i in ln:
    if isinstance(i,int):
        temp=i
        rev=0
        for j in ln:
            if temp!=0:
                r=temp%10
                rev=rev*10+r
                temp=temp//10
        out.append(rev) #this is a list so we have to append out answers
print(out)
'''
'''
#Q2:
s='power star'
word=s.split()
out={}
for i in word:
    count=0
    for j in i:
        if j in 'aeiou':
            count+=1
            out[i]=count
print(out)
'''
'''
#Q3;
s=input("Enter the string: ")
res=''
for i in s:
    if i in '!@#$%^&*':
        res+=' '
    else:
        res+=i
print(res)
'''
'''
#Q4:
t = (1, [2, 3], (4, 5), {6, 7})
r=[]
for i in t:
    if type(i)==list:
        r.append(i)
    elif type(i)==set:
        r.append(i)
    #else:
        #print("The tuple does't have any mutable values")
print(r)
'''
#--------------Functions------------------
'''
#1-Without argument without return type
def n(): #no arguments
    for i in range(1,11):
        print(i,end=' ') #No return type
n()
'''
'''
#2-with arguments with return type. 
def num(a): #with arguments
    n=[]
    for i in range(a):
        n.append(i)
    return n  #with return type
print(num(11))
'''

'''
#3-without arguments with return type. 
def num(): #without arguments with return type
    n=[]
    for i in range(11):
        n.append(i)
    return n  
print(num())
'''
'''
#4-with arguments without return type. 
def num(a): #with arguments without return type.
    n=[]
    for i in range(a):
        n.append(i)
    print(n)  
num(11)
'''
'''
#Q: write a funtion program for palindrome or not.
def palin(s):
      if s[::-1]==s:
            return f'the string {s} is palindrome'
      else:
            return 'it is not a palindrome'
string=input('Enter a string')
print(palin(string))
'''
'''
#Q: write a funtion program for prime or not. 
def prime(n):
    if  n<1:
          return False
    for i in range(2,n//2+1): #This is the time efficient code for finding prime numbers.
        if n%i==0:
                return False
        return True
print(prime(23))
'''     
'''
#random guessing game.       
import random
games=['a','b','c']
play=random.choice(games)
print(play)
'''

'''
def prime(n):
    if  n<1:
          return "Enter a positive number from 2"
    for i in range(2,n//2+1):                   
        if n%i==0:
             return f"{n} is not a prime number"
    return f"{n} is a prime number"
print(prime(14))
'''