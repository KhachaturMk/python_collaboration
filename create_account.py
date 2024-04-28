import random
def unique_number():
    random_number = random.randint(0000, 9999)
    acc_number = 'TB' + str(random_number)
    return acc_number

def account_details(name, balance):
    try:
        if balance.isdigit and int(balance) in range(0, 101):
            return {'name': name, 'balance': int(balance)}
    except ValueError:
        print('Incorrect starting balance')

