import random
import time
import sys
accountBal = 5000
custormer_info = {}
wuiuoaww4r

def homepage():
    print('''Welcome to access bank. Your satisfaction is our priority.\nEnter 1 to register\nEnter 2 to login\nEnter 3 to quit''')
    done = int(input(""))
    if done == 1:
        Register()
    elif done == 2:
        login()
    elif done == 3:
        sys.exit
    else:
        print("i dont know what you want. you are to pick between 1 or 2 to perform any action")
        homepage()

def Register():
    accountNum = random.randint(1000000000, 9999999999)
    firstName = input("Enter your first name: ").capitalize()
    lastName = input("Enter your last name: ").capitalize()
    password = input("Enter your password: ")
    while len(password) <= 4:
        print("password must be greater than 4 character")
        password = input("Enter your password: ")
    confirmPas = input("Confirm your password : ")
    while confirmPas != password:
        print("password is incorrect.")
        password = input("Enter your password: ")
        confirmPas = input("Confirm your password : ")
    phoneNo = input("enter your phone number: ")
    while len(phoneNo) != 11:
        print("your phone number must be 11 digits")
        phoneNo = input("enter your phone number: ")
        time.sleep(3)
    print(f"""Welcome {lastName} {firstName}, You have succesfully created an account and your Account number is {accountNum}, 
          and your opening account balance is {accountBal}. thanks for trusting us.""")
    custormer_info.update({accountNum:[lastName,firstName,phoneNo,password,accountBal]})
    print(custormer_info)
    login()

def login():
    global user_account
    user_account = int(input("Enter your account number: "))
    if user_account in custormer_info.keys():
        user_password = input("Enter your password: ")
        if user_password == custormer_info[user_account][3]:
            print(f"Login in successful {custormer_info[user_account][0]} {custormer_info[user_account][1]}")
            time.sleep(2)
            operation()
        else:
            print("password not correct. please try again")
            login()
    else:
        print("Account not found.\nEnter 1 to try again\nEnter 2 to register\nenter 3 to terminate the program")
        user_choice =int(input(""))
        if user_choice == 1:
            login()
        elif user_choice == 2:
            Register()
        else:
            print("i dont understand what you mean")
            homepage()

def operation():
    print("Welcome.\nEnter 1 to check balance\nEnter 2 to deposit\nEnter 3 to withdraw\nEnter 4 to transfer\nEnter 5 to go back to home page")
    user_choice = int(input(""))
    if user_choice == 1:
        checkBal()
    elif user_choice == 2:
        deposit()
    elif user_choice == 3:
        withdraw()
    elif user_choice == 4:
        transfer()
    else:
        homepage()

def checkBal():
    print(f"Dear {custormer_info[user_account][0]} ,your Account balance is {custormer_info[user_account][4]}. Thank you")
    operation()

def deposit():
    amount = float(input("how much do you want to deposit: "))
    new_balance = custormer_info[user_account][4] + amount
    custormer_info[user_account][4] = new_balance
    print(f" Txn: credit  N{amount} has been added to your account. Your new account balance is {new_balance} ")
    operation()

def withdraw():
    amount = int(input("How much do you want to withdraw: "))
    while amount > custormer_info[user_account][4]:
        print("you are having insufficient balance")
        amount = int(input("How much do you want to withdraw: "))
    else:
        new_balance = custormer_info[user_account][4] - amount
        custormer_info[user_account][4] = new_balance
        print(f" txn: N{amount} has been debited from your account. Your new account balance is N{new_balance}")
        operation()

def transfer():
    balance = custormer_info[user_account][4]
    recipent = int(input("Enter the account number: "))
    if recipent in custormer_info.keys():
        print(f" you are currently transferring to  {custormer_info[recipent][0]} {custormer_info[recipent][1]} ")
        amount = int(input("enter the amount you want to send: "))
        while amount > balance:
            print("you dont have sufficient balance")
            amount = int(input("enter the amount you want to send: "))
        else:
            new_amt = balance - amount
            custormer_info[user_account][4] = new_amt
            recipentBal = custormer_info[recipent][4] + amount
            custormer_info[recipent][4] = recipentBal
            print("succesful")
            print(f'''you have succesfully  transferred {amount} to {custormer_info[recipent][0]} {custormer_info[recipent][1]},
            Your new account balace is {new_amt} ''')
            operation()
    else:
        print("account not found")
        operation()

homepage()


        




w
