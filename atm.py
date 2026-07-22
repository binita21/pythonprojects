import random
from datetime import datetime


class ATM:

    def __init__(self, total_balance):
        self.total_balance = total_balance

    def user_info(self, name, accountno, pin):
        self.name = name
        self.accountno = accountno
        self.__pin = pin
        print(f"Your account info is:\n Name = {self.name}\n Account Number = {self.accountno}")

    def __pininfo(self):
        return self.__pin

    def check_balance(self):
        print(f"Total balance in your account is: {self.total_balance}")
        return self.total_balance

    def deposit_money(self):
        amount = float(input("Enter the amount to deposit: "))
        if amount <= 0:
            print("Invalid amount! Deposit must be greater than 0.")
            return
        self.total_balance += amount
        print(f"Dear user {self.name},your account {self.accountno} is credited by NPR {amount} on {datetime.today()}.")
        print(f"Your current balance is NPR{self.total_balance}")

    def withdraw_money(self):
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= 0:
            print("Invalid amount! Withdrawal must be greater than 0.")
            return
        if self.total_balance >= amount:
            self.total_balance -= amount
            print(f"Dear user {self.name},your account {self.accountno} is debited by NPR {amount} on {datetime.today()}.")
            print(f"Your current balance is NPR{self.total_balance}")
        else:
            print("Insufficient balance.")

    def __reset_pin(self):
        print("To reset your pin, please enter your current pin.")
        input_pin = input("Pin : ")
        if input_pin == self.__pininfo():
            newpin = input("Enter new pin : ")
            self.__pin = newpin
            print("Pin reset sucessfully!")
        else:
            print("Invalid pin, Enter the OTP sent to your mobile number for verfication.")
            OTP = random.randint(1000, 9999)
            print(f"OTP : {OTP}")
            try:
                input_otp = int(input("Enter OTP :  "))
            except ValueError:
                print("Invalid OTP format!")
                return
            if input_otp == OTP:
                newpin = input("Enter new pin : ")
                self.__pin = newpin
                print("Pin reset successfully!")
            else:
                print("Invalid OTP!")

    def __get_choice(self):
        while True:
            try:
                choice = int(input("Enter choice (1-5)\n"))
                if choice in range(1, 6):
                    return choice
                else:
                    print("Invalid choice! choose between 1 to 5")
            except ValueError:
                print("Value Error! Please enter number.")

    def __verify_pin(self, action_name):
        pin_attempts = 0
        pin_guess = input(f"Enter your pin to {action_name}: ")

        while pin_guess != self.__pininfo():
            pin_attempts += 1
            if pin_attempts >= 3:
                print("Too many incorrect attempts!")
                print("Your card is blocked for 24 hours, Try again later!")
                return False
            print("Invalid Pin, Try again!")
            pin_guess = input(f"Enter your pin to {action_name}: ")

        return True

    def features(self):

        self.choice_list = ['Check Balance', 'Deposit Money', 'Withdraw Money', 'Reset Pin', 'Cardless Transactions']

        while True:
            print("Welcome to MYBank Atm.\nWhat feature do you want to use?\n1.Check Balance\n2.Deposit Money\n3.Withdraw Money\n4.Reset Pin\n5.Cardless Transactions ")
            self.choice = self.__get_choice()

            pin_verified = self.__verify_pin(self.choice_list[self.choice - 1])
            if not pin_verified:
                break

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

            again = input("\nDo you want to perform another operation? (y/n): ").strip().lower()
            if again != 'y':
                print("Thank you for using MYBank Atm. Goodbye!")
                break
            print()


a = ATM(100000)
a.user_info("John Doe", 1234567890, '1234')
a.features()