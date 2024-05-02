from print_options import printLines

def display_history(db):
    acc_number = input("Enter your account number: ")
    key = db.get(acc_number)
    if key is not None:
        for values in key:
            printLines()
            print(f"Transaction history for {values['name']} ({acc_number}):")
            for transaction in values['history']:
                print(transaction)
    else:
        printLines()
        print("Account not found")

def filter_history(db):
    acc_number = input("Enter your account number: ")
    key = db.get(acc_number)
    if key is not None:

        filter_choice = input("Choose (Deposit/Transfer): ")
        if filter_choice == "Deposit":
            for values in key:
                for transaction in values['history']:
                    if transaction.startswith("Deposit:"):
                        print(transaction)

        elif filter_choice == "Transfer":
            for values in key:
                for transaction in values['history']:
                    if transaction.startswith("Transfer"):
                        print(transaction)
        
        else:
            printLines()
            print("Incorrect Input")
       
    else:
        printLines()
        print("Account not found")


def history_options(db):
    printLines()
    user_option = input("Enter your Option (Filter/History): ")
    if user_option == "Filter":
        filter_history(db)
    elif user_option == "History":
        display_history(db)
    else:
        printLines()
        print("Invalid Option")