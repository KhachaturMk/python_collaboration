from print_options import printLines
from csv_reader import load_data
from user import User
from accounts import checking_user_validity,generating_user

#import pandas as pd
#import uuid
import csv
import datetime


class Bank:
    def __init__(self):
        self.users = load_data("users.csv")
        self.transactions = load_data("transactions.csv")
        self.loan = load_data("loan_payment_plan.csv")

    def add_account(self):
        user = generating_user()
        checking_user_validity(user,self)
    
    def top_up_balance(self):
        printLines()
        acc_number = input("Enter your account number: ")
        balance = float(input("Enter top up balance: "))
        Users = load_data("users.csv")
        duplicate_found = False
        for row in Users:
            if row[2] == acc_number:
                duplicate_found = True
                row[3] = float(row[3]) + balance
                print(f"current balance is: {row[3]}")

                with open("users.csv", mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(Users)

                csvfile = open('transactions.csv', mode='a', newline='', encoding='utf-8')
                now = datetime.datetime.now()
                csvfile.write(f"Top up,Sender: {row[1]},{row[2]}, Receiver: {row[1]},{row[2]},{balance},{now.strftime('%Y-%m-%d %H:%M:%S')}\n")

                break
        if not duplicate_found:
            print("user does not exist")

    def transfer_money(self):
        printLines()
        sender_acc_number = input("Enter sender's account number: ")
        reciever_acc_number = input("Enter receiver's account number: ")
        
        Users = load_data("users.csv")
        sender_exists = False
        reciever_exists = False
        available_money = 0

        for row in Users:
            if row[2] == sender_acc_number:
                sender_exists = True
                available_money = float(row[3])
            if row[2] == reciever_acc_number:
                reciever_exists = True

        if sender_exists != True and reciever_exists == True:
            print("sender does not exist")

        if sender_exists == True and reciever_exists != True:
            print("reciever does not exist")

        if sender_exists != True and reciever_exists != True:
            print("both invalid users")    

        if sender_exists == True and reciever_exists == True:
            try:
                transfer_amount = float(input("Enter transfer amount: "))
                if transfer_amount < available_money:
                    for row in Users:
                        if row[2] == sender_acc_number:
                            sender_info = row
                            row[3] = float(row[3]) - transfer_amount

                        if row[2] == reciever_acc_number:
                            reciever_info = row
                            row[3] = float(row[3]) + transfer_amount
                    
                    with open("users.csv", mode='w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(Users)

                    printLines()
                    print(f"{transfer_amount} GEL was transferred from {sender_acc_number} to {reciever_acc_number}")
                    print(f"Sender:{sender_info[1]}\t IBAN code:{sender_info[2]}\t Balance:{sender_info[3]}")
                    print(f"Receiver:{reciever_info[1]}\t IBAN code:{reciever_info[2]}\t Balance:{reciever_info[3]}")

                    csvfile = open('transactions.csv', mode='a', newline='', encoding='utf-8')
                    now = datetime.datetime.now()
                    csvfile.write(f"Transfer,Sender: {sender_info[1]},{sender_info[2]}, Receiver: {reciever_info[1]},{reciever_info[2]},{transfer_amount},{now.strftime('%Y-%m-%d %H:%M:%S')}\n")
            except ValueError:
                print("Error: Invalid input. Please enter a numeric value.")

    def user_info(self):
        printLines()
        acc_number = input("Enter Iban Code for information: ")
        Users = load_data("users.csv")
        user_exists = False
        for row in Users:
            if row[2] == acc_number:
                user_exists = True
                printLines()
                print(f" Iban Code: {acc_number}\n Name: {row[1]}\n Balance: {row[3]}")
        if user_exists == False:
            print("User Does not exist")

    def transaction_history(self):
        printLines()
        acc_exist = False
        acc_number = input("Enter your account number: ")
        history = load_data("transactions.csv")

        for row in history:
            if row[2] == acc_number or row[4] == acc_number:
                acc_exist = True
                break

        if acc_exist == True:        
            user_option = input("1.History\n2.Filter\nEnter your Option: ")        
            if user_option == "1":                             
                for row in history:
                    if row[2] == acc_number or row[4] == acc_number:
                        printLines()  
                        print(f"| Type:{row[0]} | {row[1]} | Sender IBAN code:{row[2]} |{row[3]} | Reciever IBAN code:{row[4]} | Amount:{row[5]} | Date:{row[6]} |")
                    
            elif user_option == "2":
                filter_choice = input("1.Deposit\n2.Transfer\nEnter your Option:")
                if filter_choice == "1":             
                    for row in history:
                        if row[0] == "Top up" and (row[2] == acc_number or row[4] == acc_number):
                            printLines()  
                            print(f"| {row[1]} | Sender IBAN code:{row[2]} |{row[3]} | Reciever IBAN code:{row[4]} | Amount:{row[5]} | Date:{row[6]} |")

                elif filter_choice == "2":
                    for row in history:
                        if row[0] == "Transfer" and (row[2] == acc_number or row[4] == acc_number):
                            printLines()  
                            print(f"| {row[1]} | Sender IBAN code:{row[2]} |{row[3]} | Reciever IBAN code:{row[4]} | Amount:{row[5]} | Date:{row[6]} |")
                else:
                    printLines()
                    print("Incorrect Input")
            else:
                printLines()
                print("Invalid Option")
        else:
            printLines()
            print("account does not exist")

    def loan_calculator(self):
        LOAN_INTEREST = 8.2/100
        LOAN_TERM_MONTHS = 12

        printLines()
        acc_number = input('Enter your account number: ')
        loan_amount = input('Enter loan amount: ')
        Users = load_data("users.csv")
        for row in Users:
            if row[2] == acc_number:
                user_info = row

        
        if user_info is not None and loan_amount.isdigit() and float(loan_amount) > 0:
            loan_amount = float(loan_amount)
            print(f"\nOur interest is {LOAN_INTEREST*100} % per year")

            answer = input('Do you want to take a loan? (y/n): ')
            if answer == 'y':
                
                user_info[3] = float(user_info[3]) + float(loan_amount)
                print(f"\n{loan_amount} GEL was added to the balance")
                print(f" Iban Code: {user_info[2]}\n Name: {user_info[1]}\n Balance: {user_info[3]}")

                with open("users.csv", mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(Users)

                monthly_interest_rate = LOAN_INTEREST / 12
                monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate)**LOAN_TERM_MONTHS) / ((1 + monthly_interest_rate)**LOAN_TERM_MONTHS - 1)

                csvfile = open('loan_payment_plan.csv', mode='a', newline='')
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(['Month', 'Starting Balance', 'Interest Payment', 'Principal Payment', 'Ending Balance'])

                total_paid = 0
                for month in range(1, LOAN_TERM_MONTHS + 1):
                    interest_payment = loan_amount * monthly_interest_rate
                    principal_payment = monthly_payment - interest_payment
                    total_paid += monthly_payment

                    csvwriter.writerow([f'{month:<3}', f'{loan_amount: >15.2f}', f'{interest_payment: >15.2f}', f'{principal_payment: >15.2f}', f'{loan_amount - principal_payment: >15.2f}'])
                    loan_amount -= principal_payment
                csvwriter.writerow(['Total Amount to be Paid', f'{total_paid:.2f}'])

                csvfile.close()
                print(f"Total amount to be paid over {LOAN_TERM_MONTHS} months: {total_paid:.2f} GEL")

            else:
                printLines()
                print('For detailed information you can call us')
            
        else:
            printLines()
            print('Incorrect account number or loan amount')