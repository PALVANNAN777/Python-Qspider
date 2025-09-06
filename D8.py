'''#Conditional Statements..........
bill=int(input("Enter the total billing amount:"))
if bill>= 5000:
    print("You have won a offer!!")
else:
    print("Offer not applicabele")
print("Thank you for shopping...")
'''
'''
sal=int(input("Enter your salary: "))
exp=int(input("Enter your number of working years:"))
if exp >=5:
    print("Your gratituty amount :",sal*2)
else:
    print("You have to complete five years of working")
'''
'''
bal=50000
withdraw=int(input("Enter your withdraw amount: "))
if bal < withdraw:
    print("Insufficient balance")
    print(f"Your Bank Balance {bal}")
else:
    bal-=withdraw
    print(f"{withdraw}$ Withdraw completed")
    print(f"Remaing Balance: {bal}$")
'''
'''
#menu={'Biriyani': 1,'Dosa':2,'Vada curry':3}
print("Choose 1 for Biriyani, 2 for Dosa , 3 for Vada curry")
ch=int(input("Enter your choice:"))
if ch==1:
    print("Ordered Biriyani")
elif ch==2:
    print("Ordered Dosa")
elif ch==3:
    print("Ordered Vada curry")
else:
    print("Invalid choice, choose form 1-3")
'''

#.......rock, paper, sissor game creation.......
import random
ch=['rock','paper','scissor']
plr=0
sys=0
print("- - - THE GAME STARTS - - -")
print("--> Enter your choice as rock or scissor or paper")
print("--> Click S to check the scores or e to end the game")
while True:
    usr=input('Enter your choice:')
    comp=random.choice(ch)
    print(f"computer choosed: {comp}")
    if usr == comp:
        print('game tie ')
        print()
    elif usr=='rock':
        if comp=='paper':
            print('Computer Wins! 🦾')
            sys+=1
            print()
        else:
            print("You Won!!! 🎉")
            plr+=1
            print()
    elif usr=='paper':
        if comp=='scissor':
            print("Computer Wins! 🦾")
            sys+=1
            print()
        else:
            print("You Won!!! 🎉")
            plr+=1
            print()
    elif usr=='scissor':
        if comp=='rock':
            print("Computer Wins! 🦾")
            sys+=1
            print()
        else:   
            print("You Won!!! 🎉")
            plr+=1
            print()
    elif usr=='s':
        print("Your Score 👦 : ",plr)
        print("System score 🤖 : ",sys)
        print()
    elif usr=='q':
        if plr>sys:
            print("THE PALYER WON THE GAME ")
        elif plr<sys:
            print("THE SYSTEM WON THE GAME ")
        else:
            print("THE GAME TIED 🤝🏻")
        print("SEE YOU NEXT TIME 😊 ")
        break
    else:
        print("Invalid choice Da Mame 😆")
        print()

