'''#-----Looping statements-------
#Q1: prog to print 5 natural numbers
i=1
while i<=5:
    print(i,end=" ")
    i+=1
#Always be aware of infinite iteration loop because it may cause our system to crash.
'''
'''
#Q2: write a program to print the numbers between the user range
n1=int(input("Enter the starting number:  "))
n2=int(input("Enter the ending number:"))
while n1<=n2:
    print(n1,end=" ")
    n1+=1
'''
'''
#Q3: write a prog to print the even numbers with the users range
n1=int(input("Enter the starting number:  "))
n2=int(input("Enter the ending number:"))
while n1<=n2:
    if(n1%2==0):
        print(n1,end=" ")
    n1+=1
'''
'''
#Q4: write a program to print table of the user input number
n1=int(input("Enter the tables you want: "))
i=1
while i<=10:
    print(i,"X",n1,"=",i*n1)
    i+=1
'''
'''
#Q5: write program to print a series 10,20,30,40....
i=1
while i<=300:
    if i%10==0:
        print(i ,end=" ")
    i+=1
'''
'''
#Q6: write a prgrams to print the series 105,98,91,...7
i=int(input("Enter the input: "))
while i>=7:
    print(i,end=" ")
    i-=7
'''
'''
#Q7: write a prog to reverse a number using while loop
n=int(input("Enter the number:"))
rev=0 #this will store the reversed digit
while n!=0: #because at the end we will take all the numbers from the n and store it in another variable in reverse order.
    var=n%10 #this var(varible) will store our last digit our input. eg: 6 from 536
    rev=rev*10+var #then rev will multipy the number by 10 so that it can add the next number it it in the last iteration eg:63*10+5=635
    n=n//10 #this is used to update our initial input number Eg: after first iteration 536 becomes 53 and goes to the next iteration.
print("rev:",rev)
'''
'''
#Q8: program to find the sum of the digit
n1=int(input("Enter the number: "))
sum=0 #varible to store the sum of the digits.
while n1!=0: #loop runs untill we extract all the numbers from n1 using // operation.
    v=n1%10 #variable v stores the last digit of the inupt digit.
    sum=sum+v #sum variable stores the variables that is being added from the last no. to the first no.
    n1=n1//10 # then we update the value of the n1.
print("The sum of the digits: ",sum) 
'''
'''
#Q9: Program to check the numbers is strong number or not.
# The concept of armstrong number is we cube every digit and add them similarly we find factorial for every digit and we add them together.  
n1=int(input("Enter the number: "))
temp=n1
sum_fact=0 #varible to store the sum of the digits.
while temp > 0: #loop runs untill we extract all the numbers from n1 using // operation.
    digit=temp%10 #variable v stores the last digit of the inupt digit.
    fact=1
    i=1
    while i<=digit:
        fact*=i
        i+=1
    sum_fact+=fact
    temp=temp//10
if sum_fact==n1:
    print("strong number") 
else:
    print("Not a strong number")
#145 is a strong number.
'''
'''
#Q10: write a program to guess number game 
# This is my version after developing the code given by sir.
import random
number=random.randint(1,10)
print("======Guess the number game=====")
guess=None
attempts=0
hearts=5
while True:
    if hearts!=0:
        guess=int(input("Enter the guess number: "))
        attempts+=1

        if guess > number:
            print("Number is higher,guess a lower number")
            hearts-=1
        elif guess < number:
            print("Number is lower,guess a higher number")
            hearts-=1
        elif guess==number:
            print("Excellent you guessed it right")
            print(f"You took {attempts} attempts")
            break
        else:
            print("Invalid input")
    else:
        print(f"\n You are out of hearts 💔 the answer is  {number}")
        break
'''
'''
# Q11:Fibonacci series
n=int(input("Enter the number of terms: "))
a,b=0,1
count=0
while(count<n):
    print(a,end=' ')
    a,b=b,a+b
    count+=1
'''
'''
#------------For Loop--------------------
#Q12:for loop to print first 5 natural numbers
for i in range(1,6):
    print(i,end=' ')
'''
'''
#Q13:write a program to print the numbers between the user range using for loop
st=int(input("Enter the number: "))
ed=int(input("Enter the ending number: "))
for i in range(st,ed+1):
    print(i,end=' ')
'''
'''
#Q14:find the length of the collection using for loop  
col=eval(input("Enter the collection: "))
count=0
for i in col:
    count+=1
print(f"the length of the collection is {count}")
'''
'''
#Q15: program to print all the string inside the list
#in=[1,2,3,"ram",[1,2,3],'hari',3,6]
#out=['ram','hari']
#Method 1:My method after getting idea from Sir's code.
col=eval(input("Enter the collection: "))
#count=0
out=[]
for i in col:
    if isinstance(i,str):
        out=[i]
        print(out)
'''
''''
#Method 2:Sir's method.
col=eval(input("Enter the collection: "))
out=[]
for i in col:
    if type(i)==str:
        out+=[i]
print(out)
'''
'''
#program to reverse the string present in this collection
col=eval(input("Enter the collection: "))
out=[]
for i in col:
    if type(i)==str:
        out+=[i[::-1]] # or inside the if loop declare s=i[::-1] and change out+=[s]
print(out)
'''
#'''
#Q16: program to print all the string inside the list
#in=[1,2,3,"nitin",[1,2,3],'hari',3,6,'malayalam']
#out=['nitin','malayalam']
#print the string only if it in palindrome
col=eval(input("Enter the collection: "))
out=[]
for i in col:
    if type(i)==str:
        s=i[::-1]
        if s==i:
            out+=[i]
print(out)
#'''