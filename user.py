from print_options import printLines

import random

class User:
    def __init__(self):
        self.name = None
        self.balance = 0
        self.iban_code = None

    def set_name(self):
        self.name = input("Enter Your name: ")
    
    def set_balance(self):
        while True:
            try:
                balance = float(input("Enter your balance (0-100): "))
                if 0 <= balance <= 100:
                    self.balance = balance
                    break
                else:
                    print("The amount you entered is out of range. Please enter a value between 0 and 100.")
            except ValueError:
                print("Error: Invalid input. Please enter a numeric value.")            
    
    def set_ibancode(self):
        self.iban_code = self.generate_unique_number()

    def generate_unique_number(self):
        random_number = random.randint(0, 9999)
        while len(str(random_number)) != 4:
            random_number = random.randint(0, 9999)
        return 'TB' + str(random_number)
    
    def get_name(self):
        return self.name
    
    def get_balance(self):
        return self.balance
    
    def get_ibancode(self):
        return self.iban_code