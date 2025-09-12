'''#=========RECURSION==========
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(10))
'''
'''
#WRP to find sum of all digits using recursion [ERROR]
def sum_of_digit(n):
    if n==0:                                                 #n%10 contains the last number. Eg. 3 form the number 123
        return 0                                              
    else:
        return n%10+sum_of_digit(n//10)                     #n//10 updates the number after taking the last digit. Eg. 12 after taking 3 from 123.
print(sum_of_digit(555))
'''

'''
#WRP to find the sum of the previous numbers
def n_numbers(n):
    if n==0:
        return 0
    else:
        return n+n_numbers(n-1)
print(n_numbers(3))
'''
'''
#While to recursion conversion.
#While loop formate
s=input("Enter a string: ")
out=' '
i=0
while i<len(s):
    if 'a'<=s[i]<='z':
        out+=s[i]
    i+=1
print(out)
'''
'''
#Recursion formate
def ext_low(s,out='',i=0):
    if i>len(s)-1:                  
        return out
    if 'a'<=s[i]<='z':
        out+=s[i]
    return ext_low(s,out,i+1) #Updation
s=input("Enter a string:")
print(ext_low(s))
'''
#WRP to display the following pattern
#IN = 3
#OUT= 3 2 1 2 3
'''
def sam(n):
    print(n,end=' ')
    if n==1:
        return
    sam(n-1)
    print(n,end=' ')
sam(3)
'''
#=========Leet code & Hacker rank questions============
'''
#Question-1           #My code with small help form sir.
def leap(n):
    if n%4==0 and n%100!=0:
        print("true")
    elif n%100==0:
        if n%400==0:
            print("true")
        else:
            print("false")
    else:
        print("false")
s=int(input("Enter the year: "))
leap(s)
'''

#Question-2:
'''
s=list(map(int,input("Enter the list elements:").split()))
ch=input("Enter the element to find:")
for i in s:                                                           #My attempt [ERROR]
    if i==ch:
        print('The sencond largest Element:',i)
'''
'''
def runner_up(score):    #Sir's code
    s=sorted(score)
    out=[]
    for i in s:
        if i not in out:
            out.append(i)
    return out[-2]
scores=eval(input("Enter the scores: "))
print(runner_up(scores))
'''
#Question-3:
#IN= abcdefgh 
#2
#out=ab
#cd 
#ef 
#gh
'''
def wrap(a):      #My attempt                  
    out=[]
    for i in a:
        out.append(i)
    print(out)
string="abcdefgh"
print(wrap(string))
'''
'''
def wrap(s,max_width):     #Sir's code
    for i in range(0,len(s),max_width):
        print(s[i:i+max_width])
s="ABCDEFGH"
max_width=2
wrap(s,max_width)
'''
'''
#Question-4:
#Input=23
#out='ad'
#'ae'
#'af'
#'bd'
#'be'
#'bf'
#'cd'
#'ce'
#'cf'
#phone={1:[],2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
def call(phone,choice):
    for choice in phone:
        print()
phone={1:[],2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
choice=input("Enter the number: ")
call(phone,choice)
'''
'''
def combinations(digits):
    d={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    if digits in ['0','1',' ']:
        return []
    if len(digits)==1 and digits in d:
        return list(d[digits])
    elif len(digits)==2 and digits in d:
        s1=d[digits[0]]
        s2=d[digits[1]]
        out=[]
        for i in s1:
            for j in s2:
                if i != j:
                    out.append(i+j)
        return out
digits=input("Enter the digit:")
print(combinations(digits))
 '''       
