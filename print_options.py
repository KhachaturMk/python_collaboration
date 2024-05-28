def operation_options():
    printLines()
    print("1. create account")
    print("2. top up balance")
    print("3. transfer money")
    print("4. account details")
    print("5. transaction history")
    print("6. loan calculator\n")
    print("0. Exit\n")

    user_input = input("Enter Your Option: ")
    return user_input

def printLines():
    print("-" * 150)