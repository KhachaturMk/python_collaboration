from print_options import operation_options, printLines
#from user import User #check_account_inputs,top_up_balance
from bank import Bank
from loan import loan_calculator
from money_Transfer import  checkTransfer
from user_Information import user_Info
from history import history_options

bank = Bank()

while True:
    select = operation_options()
    if select == '1':
        bank.add_account()

    elif select == '2':
        bank.top_up_balance()

    elif select == '3':
        bank.transfer_money()

    elif select == '4':
        bank.user_info() 

    elif select == '5':
        bank.transaction_history()   

    elif select == '6':
        bank.loan_calculator()

    elif select == '0':
        print('Exit')
        exit()

    else:
        printLines()
        print("Invalid input")