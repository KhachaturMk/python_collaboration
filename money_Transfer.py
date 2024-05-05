from print_options import printLines

def checkSender(db,sender):
    for Users in db:
        if sender == Users:
            return True
    return False

def checkReciever(db,reciever):
    for Users in db:
        if reciever == Users:
            return True
    return False

def checkBalanceMoney(db,sender):
    User = db.get(sender)
    for values in User:
        return values['balance']
    
def Transfer(db,sender,reciever,money):
    User = db.get(sender)
    for sendervalues in User:
        sendervalues['balance'] = sendervalues['balance'] - money
        sendervalues['history'].append(f"Transfer to {reciever}: -{money}")
        
    User = db.get(reciever)
    for recievervalues in User:
        recievervalues['balance'] = recievervalues['balance'] + money
        recievervalues['history'].append(f"Transfer from {sender}: +{money}")
        
    print(f"\n Iban Code: {sender}\n Name: {sendervalues['name']}\n Balance: {sendervalues['balance']}")
    print(f"\n Iban Code: {reciever}\n Name: {recievervalues['name']}\n Balance: {recievervalues['balance']}")
   
def checkTransfer(db):
    printLines()
    sender_acc_number = input("Enter sender's account number: ")
    receiver_acc_number = input("Enter receiver's account number: ")
    amount = input("Enter transfer amount: ")
    sender_key = db.get(sender_acc_number)
    receiver_key = db.get(receiver_acc_number)
    f = open('transaction.txt', mode='a')  # Open file in append mode
    if sender_key is not None and receiver_key is not None and amount.isdigit() and int(amount) > 0:
        for sender_values in sender_key:
            if sender_values['balance'] >= int(amount):
                for receiver_values in receiver_key:
                    sender_values['balance'] -= int(amount)
                    receiver_values['balance'] += int(amount)
                    sender_values['history'].append(f"Transfer to {receiver_values['name']}: -{amount}")
                    receiver_values['history'].append(f"Transfer from {sender_values['name']}: +{amount}")
                    printLines()
                    print(f"{amount} GEL was transferred from {sender_acc_number} to {receiver_acc_number}")
                    print(f"Sender: {sender_values['name']}\n Sender's Balance: {sender_values['balance']}")
                    print(f"Receiver: {receiver_values['name']}\n Receiver's Balance: {receiver_values['balance']}")
                    f.write(f"Transfer OUT: {sender_values['name']}, {sender_acc_number}, -{amount} GEL\n")  # Write transaction to file
                    f.write(f"Transfer IN: {receiver_values['name']}, {receiver_acc_number}, +{amount} GEL\n")  # Write transaction to file
            else:
                printLines()
                print("Insufficient balance")
    else:
        printLines()
        print("Incorrect account numbers or amount")
    f.close() 
