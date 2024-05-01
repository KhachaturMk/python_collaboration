from print_options import printLines

def user_Info(db):
    user = input("Enter Iban Code for information: ")
    User = db.get(user)
    if user is not None:
        for sendervalues in User:
            printLines()
            print(f" Iban Code: {user}\n Name: {sendervalues['name']}\n Balance: {sendervalues['balance']}")
    else:
        print("User doesn't exist")