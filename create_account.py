import random

def unique_number():
    random_number = random.randint(0000, 9999)
    acc_number = 'TB' + str(random_number)
    return acc_number



def account_details(name, balance):
    try:
        if balance.isdigit and int(balance) in range(0, 101):
            return {'name': name, 'balance': int(balance)}
        elif balance.isdigit and int(balance) not in range(0, 101):
            print("------------------------------------------------")
            print("The amount you entered is out of range")
    except ValueError:
        print("------------------------------------------------")
        print('The amount you enter is not a number')



def check_account_inputs(db):
    print("------------------------------------------------")
    name = input('Enter your name: ')
    balance = input('Enter starting balance (0-100): ')

    if unique_number() not in db.keys() and account_details(name,balance) is not None:
            db[unique_number()] = [account_details(name,balance)]

    print(db)

def top_up_balance(db):
    print("------------------------------------------------")
    acc_number = input('Enter your account number: ')
    balance = input('Enter top up balance: ')
    key = db.get(acc_number)
    if key is not None and balance .isdigit() and int(balance) > 0:
        for values in key:
            values['balance'] += int(balance)
            print(f"{balance} GEL was added to the balance")
            print(db)
    else:
        print('incorrect info')