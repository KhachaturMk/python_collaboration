from print_options import printLines
import csv

def loan_calculator(db):
    LOAN_INTEREST = 8.2/100
    LOAN_TERM_MONTHS = 12

    printLines()
    acc_number = input('Enter your account number: ')
    loan_amount = input('Enter loan amount: ')
    key = db.get(acc_number)
    if key is not None and loan_amount.isdigit() and int(loan_amount) > 0:
        loan_amount = int(loan_amount)
        amount_to_be_paid = loan_amount + LOAN_INTEREST*loan_amount
        print(f"\nYour annual payment will be {amount_to_be_paid} GEL")

        answer = input('Do you want to take a loan? (y/n): ')
        if answer == 'y':
            for values in key:
                values['balance'] += int(loan_amount)
                print(f"\n{loan_amount} GEL was added to the balance")
                print(f" Iban Code: {acc_number}\n Name: {values['name']}\n Balance: {values['balance']}")
        else:
            printLines()
            print('For detailed information you can call us')

        monthly_interest_rate = LOAN_INTEREST / 12
        monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate)**LOAN_TERM_MONTHS) / ((1 + monthly_interest_rate)**LOAN_TERM_MONTHS - 1)


        csvfile = open('loan_payment_plan.csv', mode='w', newline='')
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Month', 'Starting Balance', 'Interest Payment', 'Principal Payment', 'Ending Balance'])

        total_paid = 0
        for month in range(1, LOAN_TERM_MONTHS + 1):
            interest_payment = loan_amount * monthly_interest_rate
            principal_payment = monthly_payment - interest_payment
            total_paid += monthly_payment

            csvwriter.writerow([f'{month:<3}', f'{loan_amount: >15.2f}', f'{interest_payment: >15.2f}', f'{principal_payment: >15.2f}', f'{loan_amount - principal_payment: >15.2f}'])
            loan_amount -= principal_payment
        csvwriter.writerow(['Total Amount to be Paid', f'{amount_to_be_paid:.2f}'])

        csvfile.close()

      

        print(f"Total amount to be paid over {LOAN_TERM_MONTHS} months: {amount_to_be_paid:.2f} GEL")


    else:
        printLines()
        print('Incorrect account number or loan amount')