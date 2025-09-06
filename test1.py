# TEST DATE - 1/9/2025
#1. Wap to check whether the char is uppercase, lowercase, digit or special char.
'''
ch=input("enter the Character: ")
if ch>='A' and ch<='Z':
    print("The character is uppercase")
elif ch>='a' and ch<='z':
    print("The character is Lowercase")
elif ch>='0' and ch<='9':
    print("The character is Digit")
else:
    print("The character is Special character ")
'''

'''
#8. Wap to count the number of words in a string.
#Input 1: s = “ I love coding in Python ”
#Output 1: 5

S=input("Enter the string: ")
cut=S.split()
words=len(cut)
print(words)
'''

#---------OTHER CODE------

n=int(input("Enter the number:")) #error
if n%3==0:
    print("Fizz")
elif n%5==0:
    print("buzz")
elif n%3==0 and n%5==0:
    print("Fizzbuzz")
else:
    print("The number is not divisible by both 3 and 5")
