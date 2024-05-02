from print_options import printLines

def display_history(db):
    printLines()
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