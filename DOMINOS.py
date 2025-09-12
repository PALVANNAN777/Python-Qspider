#=====QSPIDER PROJECT=====#
#DAY-13 FINAL POJECT
import random
class Dominos:
    menu = {'veg': {'margerita': 129, 'cheese_and_corn': 169, 'peppi_paneer': 260, 'veg_loaded':210, 'tomato_tangi': 170},
            'non_veg': {'pepper_barbeque': 199, 'non_veg_loaded': 169, 'chicken_sausage': 200},
            'snacks': {'garlic_bread': 120, 'zingy': 59, 'chicken_cheese_balls': 170},
            'desserts': {'choco_lava': 100, 'mousse cake': 169},
            'drinks': {'coke': 90, 'pepsi': 78, 'sprite': 50}}

    def __init__(self,name,email,phno):
        self.name=name
        self.email=email
        self.phno=phno
        self.login_status=False
        self.cart={}

        while True:
            if not(self.login_status):
                print("-"*50)
                print("...........Welcome to Dominos 🍕 app..........")
                print("Login")
                ch=input("Do you want to login? (y/n): ").lower()
                if ch=='y':
                    self.login()
                else:
                    print("Login is required")
                    



            if self.login_status:
                print("...........Welcome to Dominos 🍕 app..........")
                print(f"Use 👤 :{self.name}")
                print("Enter 1: Order")
                print("Enter 2: Show cart")
                print("Enter 3:Logout")
                ch=int(input("Enter your Chice: "))
                if ch==1:
                    self.order()
                elif ch==2:
                    self.show_cart()
                elif ch==3:
                    if self.logout():
                        break
                else:
                    print("Invalid Choice")



    @staticmethod
    def validate_otp(value):
        while True:
            print("-"*50)
            og_otp=random.randint(1000,99999)
            print(f"otp sent to {value}")
            print(f"your otp is {og_otp}")

            otp=int(input("Enter the otp: ")) 
            if otp==og_otp:
                print("Login success✅") 
                return True  
            else:
                print("Invalid otp")
                
    def login(self):
        print("Enter 1: Login with Phone")
        print("Enter 2: Login with E-Mail")
        ch=int(input("Enter your choice: "))
        if ch==1:
            phno=int(input("Enter the phno: "))
            if phno==self.phno:
                print("Login successful ")
                otp=self.validate_otp(phno)
                self.login_status=otp
            else:
                print("Phno does not exist")
        elif ch==2:
            email=input("Enter the Email: ")
            if email==self.email:
                print("Login successful ")
                otp=self.validate_otp(email)
                self.login_status=otp
            else:
                print("Email does not exist")
        else:
            print("Invalid choice")

    def logout(self):
        ch=input("Do you want to logout ?(y/n): ").lower()
        if ch=='y':
            self.login_status=False
            print("Thank you for choosing Dominos")
            return True
        return False

    
    def order(self):
        while True:
            print("----------MENU----------")
            for category in Dominos.menu:
                print(category)
            print("-"*50)

            cat=input("Enter the category: ").lower()
            if cat in Dominos.menu:
                for item in Dominos.menu[cat]: #used to access the inner Dictionary
                    print(f"{item}----------Rs.{Dominos.menu[cat][item]}")
                item=input("Enter the item name: ")
                if item in Dominos.menu[cat]:
                    q=int(input("Enter the quantity: "))
                    price=q*Dominos.menu[cat][item]
                    if item in self.cart:
                        self.cart[item]+=price
                    else:
                        self.cart[item]=price
                    print(f"{item} added to cart")
                    choice=input("Do you want to add maore items or not:(y/n): ").lower()
                    if choice=='n':
                        break
                    else:
                        continue
                else:
                    print(f"{item} not available")
            else:
                print(f"{cat} not available")
            
    def show_cart(self):
        print("----------Dominos Cart----------")
        if self.cart!={}:
            total=0
            for item in self.cart:
                price=self.cart[item]
                total +=price
                print(f"{item}---------->>>Rs.{price}")
            print(f"Total price :Rs {total}")
            ch=input("If you want to place order:(y/n): ").lower()
            if ch=='y':
                print("Thank you for placeing order")
                self.cart={} #we have to empty the cart after every order the user place
            else:
                print("Cart is empty")

c1=Dominos("palvannan","palvannan.anand@gmail.com",123456789) 

