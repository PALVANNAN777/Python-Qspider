#Q1:write a function remove_duplicates(lst) without using set().
#Q2:write a function reverse_number(n) thet return the reverse of a given integer

'''
#Q1:write a function remove_duplicates(lst) without using set().
def remove_duplicates(lst):
    out=[]
    for i in lst:
            if i not in out:
                out.append(i)
    print(out)
list=[1,2,3,3,4,5]
remove_duplicates(list)
'''
'''
#Q2:write a function reverse_number(n) thet return the reverse of a given integer
def reverse_number(n):
    temp=n
    rev=0
    while temp!=0:
        v=temp%10
        rev=rev*10+v
        temp=temp//10
    return f"the reversed number is {rev}"
print(reverse_number(123))
'''

'''
# ------------LOCAL SCOPE  AND GLOBAL SCOPE---------
a=10
b=20
def sam():
    a=5
    print(a+b)# while executing this line the method will declare the value as a=10 and b-20 after checking inside and outside the method and 
#allocates the memory for them  so modifying it again will not be appplicable. But we can use global keyword to handle this situation.
    #a=5 Note: we cannot modify the varible here.
    print(a,b)
print(a,b)
sam()
print(a+b)
'''
'''
#using global
a=10
b=20
def sam():
    global a
    print(a+b)
    a=5 #Note: Because of the global keyword we can now modify the value in the global space.
    print(a,b)
print(a,b)
sam()
print(a+b)
'''
'''
#Inner function accessibility
a=10
b=20
def outer():
    m=100
    n=200
    def inner():
        print(a+b)
        print(m+n)
    inner()
print(a+b)
outer()
print(a,b)
'''
'''
#In the nested scopes we can access the global variable but we cannot modify them inside that nested scope.
#But using the nonlocal keyword we cannot modify the local variable
a=10
b=20
def outer():
    m=100
    n=200
    def inner():
        nonlocal m
        m=50
        print(m+n)
        print(m,n)
    inner()
print(a+b)
outer()
print(a,b)
'''
'''
#======PACKING AND UNPACKING=========
def single_pack(*var): #*var can be any variable name followed by *.
    #If we use var insted of *var error because we are getting 1 value for the method but we passes a tuple,list etc...
    print(type(var))
    print(var)
single_pack(10,20,30,40)
'''
'''
def double_pack(**a):
    print(type(a))
    print(a)
double_pack(a=10,b=20,c=30) #we send these valuese to store them as a dictionary
'''
'''
#===Unpacking===
def unpack(v1,v2,v3,v4):
    print(v1,v2,v3,v4)
unpack(*'aple')
'''

#Q1:print numbers from 1 to 50, Skipping all multiples of 5
#Q2:Extract only lowercase letters from a given string using continue
#Q3:WAP to count all characters in a string except spaces using continue
#Q4:WAP to search for an element in a list,if found,teminate and loop imidiately and print ''Found''
'''
#Q1:
i=1
while i<51:
    if i%5!=0:
        print(i,end=' ')
    i+=1
'''
'''
#Q2:
#method 1:My code
s=input("Enter the string:")
for i in s:
    if i>='A' and i<='Z':
        continue
    print(i,end=' ')

#method 2:Sir's code
s=input("Enter the string:")
res=' '
for i in s:
    if 'A'<=i <='Z':
        continue
    res+=i
print(res)
'''
'''
#Q3:
s=input("Enter the string: ")
count=0
for i in s:
    if i==' ':
        continue
    count+=1   
print(count)  
'''
'''
#Q4:
lst=list(map(int, input("Enter the list elements: ").split()))
ch=int(input("Enter the choice:"))
for i in lst:
    if i==ch:
        print("FOUND")
        break
    else:
        print(f"{ch}  Not Matched In The List")
'''
#----------TEST QUESTIONS PRACTICE-------------
'''
n=int(input("Enter a number: "))
if n%3==0 and n%5==0:
    print('Fizzbuzz')
elif n%3==0:
    print('Fizz')
elif n%5==0:
    print('buzz')
else:
    print("It does not satisfies our needs ")
'''
'''
print("=======INSTAGRAM LOGIN========")
usr=input("Enter your username: ")
if usr=='palvannan':
    pwd=input("enter your password: ")
    if pwd=='777':
        print("Login Successful!!")
    else:
        print("Invalid password")
else:
    print("Incorrect User name")
'''
'''
s = input("Enter the string :")
res=' '
for i in s:
    if i.isupper():
        res+=i.lower()
    elif i.islower():
        res+=i.upper()
    else:
        res+=i
print(res)
'''
'''
n=int(input("Enter the integer :"))
if n<=1:
    print("Invalid Input")
if n>=2:
    for i in range(2,n):
        if n%i==0:
            print("It is not a prime number")
    else:
        print("It is a prime number")
'''
'''
n='10100011231'
ans=' '
for i in n:
    if i=='0':
        ans+='1'
    elif i=='1':
        ans+='0'
    else:
        pass
print(ans)
'''

#14. Wap to get the following output.
#In=’abacbaacc’
#Out={‘a’:4,’b’:2,’c’:3}
'''
n='abacbaacc'
out={}
for i in n:
    count=0
    for j in n:
        if j == i:
            count+=1
    out[i]=count
print(out)
'''
'''
#Q8:
s =input("Enter a string: ")
word=s.split()
count=len(word)
print(count)
'''
'''
#Q9:
L = [10,23,6,1,8,14,19]
out=[]
for i in L:
    if i%2==0:
        out.append(i)
print(out)
'''
'''
#10. Wap to get the following output.
#S = 'power star'
#Out= {'power':'rewop', 'star':'rats'}
s='power star'
word=s.split()
out={}
rev=' '
for i in word:
    rev+=i[::-1]
    out[i]=rev                         #The syntax for the out to append in set --> out[i]=var to pass
print(out)
'''
#11. Wap to get the following output.
#S= 'always keep smiling'
#Out = 'syawla peek gnilims'
S= 'always keep smiling'
word=S.split()
rev=''
for i in word:
    rev+=i[::-1]+" "
print(rev)