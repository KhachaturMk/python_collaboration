from print_options import operation_options, printLines
from create_account import check_account_inputs, top_up_balance
from loan import loan_calculator
from money_Transfer import  checkTransfer
from user_Information import user_Info
from history import display_history

db = {}
history_db = {}

while True:
    select = operation_options()
    if select == '1':
        check_account_inputs(db)

    elif select == '2':
        top_up_balance(db)

    elif select == '3':
        checkTransfer(db)

    elif select == '4':
        user_Info(db)   

    elif select == '5':
        display_history(db)   

    elif select == '6':
        loan_calculator(db)

    elif select == '0':
        print('Exit')
        exit()

    else:
        printLines()
        print("Invalid input")
