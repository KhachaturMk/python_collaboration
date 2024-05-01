from print_options import printLines

def loan_calculator(db):
    LOAN_INTEREST = 8.2
    printLines()
    acc_number = input('Enter your account number: ')
    loan_amount = input('Enter loan amount: ')
    key = db.get(acc_number)
    if key is not None and loan_amount.isdigit() and int(loan_amount) > 0:
        amount_to_be_paid = int(loan_amount) + LOAN_INTEREST*(int(loan_amount)/100)
        print(f"\nYour annual payment will be {amount_to_be_paid} GEL")
        answer = input('Do you want to take a loan?(y/n): ')
        if answer == 'y':
            for values in key:
                values['balance'] += int(loan_amount)
                print(f"\n{loan_amount} GEL was added to the balance")
                print(f" Iban Code: {acc_number}\n Name: {values['name']}\n Balance: {values['balance']}")
        else:
            printLines()
            print('For detailed information you can call us')
    else:
        printLines()
        print('incorrect info')