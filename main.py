from print_options import operation_options
from create_account import check_account_inputs, top_up_balance
from loan import loan_calculator
db = {}

while True:
    select = operation_options()
    if select == '1':
        check_account_inputs(db)

    if select == '2':
        top_up_balance(db)

    if select == '6':
        loan_calculator(db)

    if select == '0':
        print('Exit')
        exit()