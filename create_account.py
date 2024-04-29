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