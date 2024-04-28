db = {}
from create_account import unique_number, account_details
while True:
    select = input("""1_Create account, 2_Balance, 3_Money transfer 
4_Details, 5_History, 6_Loan calculator, 0_Exit
Select operation: """)
    if select == '1':
        name = input('Enter your name: ')
        balance = input('Enter starting balance: ')

        if unique_number() not in db.keys() and account_details(name,balance) is not None:
            db[unique_number()] = [account_details(name,balance)]

    print(db)

    if select == '0':
        print('Exit')
        exit()
