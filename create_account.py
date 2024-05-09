from print_options import printLines
import random
import pandas as pd
import uuid

def unique_number():
    random_number = random.randint(0000, 9999)
    while len(str(random_number)) != 4:
        random_number = random.randint(0000, 9999)
    acc_number = 'TB' + str(random_number)
    return acc_number

def account_details(name, balance):
    try:
        if balance.isdigit and int(balance) in range(0, 101):
            return {'name': name, 'balance': int(balance), 'history': []}
        elif balance.isdigit and int(balance) not in range(0, 101):
            printLines()
            print("The amount you entered is out of range")
    except ValueError:
        printLines()
        print("The amount you enter is not a number")

def check_account_inputs(db):
    printLines()
    name = input("Enter your name: ")
    balance = input("Enter starting balance (0-100): ")
    ibanCode = unique_number()
    f = open('transaction.txt', mode='a')
    if ibanCode not in db.keys() and account_details(name,balance) is not None:
        db[ibanCode] = [account_details(name,balance)]
        user_id = uuid.uuid4()
        printLines()
        print(f"User Added Successfully\n Iban Code: {ibanCode}\n Name: {name}\n Balance: {balance}")
        f.write(f"Registration: {name}, {ibanCode}, {balance} GEL\n")
        df = pd.DataFrame([[user_id, name, ibanCode, balance]])
        df.to_csv('users.csv', header=False, mode='a', index=False)
    else:
        printLines()
        print("User already exists or incorrect input")
    f.close()

def top_up_balance(db):
    printLines()
    acc_number = input("Enter your account number: ")
    balance = input("Enter top up balance: ")
    key = db.get(acc_number)
    f = open('transaction.txt', mode='a')
    if key is not None and balance .isdigit() and int(balance) > 0:
        for values in key:
            values['balance'] += int(balance)
            values['history'].append(f"Deposit: +{balance}")
            printLines()
            print(f"{balance} GEL was added to the balance")
            print(f" Iban Code: {acc_number}\n Name: {values['name']}\n Balance: {values['balance']}")
            f.write(f"TopUp: {values['name']}, {acc_number}, {balance} GEL\n")
    else:
        printLines()
        print("incorrect info")
    f.close()