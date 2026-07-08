import random
class ATM:
    from datetime import date, datetime
    today = datetime.today()

    
    def __init__(self,total_balance):
        self.total_balance = total_balance

    def user_info(self,name,accountno,pin):
        self.name = name
        self.accountno = accountno
        self.__pin=pin
        print(f"Your account info is:\n Name = {self.name}\n Account Number = {self.accountno}",{self.__pin})
    
    def __pininfo(self):
        return self.__pin

        
    def check_balance(self):
        print(f"Total balance in your account is: {self.total_balance}")
        return self.total_balance
    

    def deposit_money(self):
        self.amount = float(input("Enter the amount to deposit: "))
        self.total_balance += self.amount
        print(f"Dear user {self.name},your account {self.accountno} is credited by NPR {self.amount} on {self.today}.")
        print(f"Your current balance is NPR{self.total_balance}")
    
    def withdraw_money(self):
        self.amount = float(input("Enter the amount to withdraw: "))
        if self.total_balance > self.amount:
            self.total_balance -= self.amount
            print(f"Dear user {self.name},your account {self.accountno} is debited by NPR {self.amount} on {self.today}.")
            print(f"Your current balance is NPR{self.total_balance}")
        else:
            print("Insufficient balance.")

    def __reset_pin(self):
        print("To reset your pin, please enter your current pin.")
        self.input_pin=input("Pin : ")
        if self.input_pin == self.__pininfo():
            self.newpin = input("Enter new pin : ")
            self.__pin = self.newpin
            print("Pin reset sucessfully!")
        else:
            print("Invalid pin, Enter the OTP sent to your mobile number for verfication.")
            OTP = random.randint(1000,9999)
            print(f"OTP : {OTP}")
            input_otp = int(input("Enter OTP :  "))
            if input_otp == OTP:
                self.newpin = int(input("Enter new pin : "))
                self.__pin = self.newpin
                print(f"Pin reset successfully!,{self.__pin}")
            else:
                print("Invalid OTP!")

        
    def features(self):
        
        print("Welcome to MYBank Atm.\nWhat feature do you want to use?\n1.Check Balance\n2.Deposit Money\n3.Withdraw Money\n4.Reset Pin\n5.Cardless Transactions ")
        self.choice_list = ['Check Balance','Deposit Money','Withdraw Money','Reset Pin','Cardless Transactions']
        
        while True:
            self.choice=int(input("Enter choice (1-5)\n"))
            try:
                if self.choice in range(1,6):
                    break
                else:
                    print("Invalid choice! choose between 1 to 5")
            except:
                print("Value Error! Please enter number.")


        pin_guess = input(f"Enter your pin to {self.choice_list[self.choice-1]}: ")
        pin_attempts=0
        while pin_guess != self.__pin and pin_attempts < 2:
            print("Invalid Pin, Try again!")
            pin_guess = input(f"Enter your pin to {self.choice_list[self.choice-1]}: ")
            pin_attempts+=1
            if pin_attempts >= 2:
                print("Too many incorrect attempts! .")
                print("Your card is blocked for 24 hours, Try again later!")
                
                
            
        if pin_guess == self.__pin:
            if self.choice == 1:
                self.check_balance()
            elif self.choice == 2:
                self.deposit_money()
            elif self.choice == 3:
                self.withdraw_money()
            elif self.choice == 4:
                self.__reset_pin()
            elif self.choice == 5:
                print("Cardless transactions are currently unavailable, Try again later!")
                    

                    
        
a = ATM(100000)
a.user_info("John Doe",1234567890,'1234')
a.features()
print(a._ATM__pininfo())
# a.check_balance()
# a.deposit_money()
# a.withdraw_money()
# a.__getattribute__("_ATM__reset_pin")() 
