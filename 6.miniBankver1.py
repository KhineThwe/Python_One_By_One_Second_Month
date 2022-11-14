#miniBanking
#ver 1
#ver 2 file
#cryptography
#ver 3 dsa
#ver 4 real world formula
#ver 5 django
import random
class Bank:
    def __init__(self):
        self.accounts = {} #{111:("ncc","222",1000)}
        self.current_accountno = None
        self.name = None
        self.password = None
        self.initial_deposit = None
        print("\t\tWelcome from NCC Bank!")

    def beautify_print(self,message):
        print("******************")
        print(message)
        print("******************")

    def create_account(self,name,password,initial_deposit):
        account_no = random.randint(100,999)
        self.accounts[account_no] = [name,password,initial_deposit]
        self.name = self.accounts[account_no][0]
        self.password = self.accounts[account_no][1]
        self.initial_deposit = self.accounts[account_no][2]
        self.current_accountno = account_no
        self.beautify_print(f'Account created successfully!your account number is {account_no}')
        print(self.accounts)
        print(self.name)
        print(self.password)
        print(self.initial_deposit)


    def register(self):
        print("This is from registration: ")
        uname = input("Please enter your name to register: ")
        upassword = input("Please enter your password to register: ")
        confirm_password = input("Please enter your password again to confirm: ")
        if upassword!=confirm_password:
            print("Passwords are not equal!")
            self.register()
        else:
            uamount = int(input("Please enter amount to register: "))
            self.create_account(uname,upassword,uamount)
            print(f"Your current account number: {self.current_accountno}")

    def main_menu(self):
        while 1:
            print("\t\tPress 1 to Register")
            print("\t\tPress 2 to Login")
            print("\t\tPress 3 to Quit")
            ch = input("\t\tPlease enter 1,2,3")
            if ch == '1':
              self.register()
            elif ch == '2':
              print("This is from login")
            elif ch == '3':
              print("Bye Bye")
              exit(1)
            else:
                print("Invalid option")

if __name__ == "__main__":
    bank = Bank()
    bank.main_menu()
