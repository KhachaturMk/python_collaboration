from user import User
from print_options import printLines

import uuid
import pandas as pd

def generating_user():
    printLines()
    user = User()
    user.set_name()
    user.set_balance()
    user.set_ibancode()
    return user

def checking_user_validity(user,bank):
    while True:
            duplicate_found = False
            for row in bank.users:
                if row[2] == user.get_ibancode():
                    print("Error: User already exists with the same IBAN code. Generating new IBAN code...")
                    duplicate_found = True
                    user.set_ibancode()
                    break
                
            if not duplicate_found:
                user_id = uuid.uuid4()
                printLines()
                print(f"User Added Successfully\n Iban Code: {user.get_ibancode()}\n Name: {user.get_name()}\n Balance: {user.get_balance()}")
                df = pd.DataFrame([[user_id, user.get_name(), user.get_ibancode(), user.get_balance()]])
                df.to_csv('users.csv', header=False, mode='a', index=False)
                break