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
    sender = input("Enter Your ID: ")
    reciever = input("Enter recievers ID: ")
    if checkSender(db,sender) == True and checkReciever(db,reciever) == True:
        while True:

            try:
                printLines()
                print(f"Your Current Amount of Money ({checkBalanceMoney(db,sender)})") 
                moneyAmount = int(input("Enter Amount of money to send: "))                                
            except ValueError:
                printLines()
                print("The amount you enter is not a number")

            if int(checkBalanceMoney(db,sender)) > moneyAmount:
                Transfer(db,sender,reciever,moneyAmount)
                
                break
            else:
                printLines()
                print("Not enought funds")

    elif checkSender(db,sender) == False and checkReciever(db,reciever) == True:
        printLines()
        print("Sender user doesn't exists")

    elif checkSender(db,sender) == True and checkReciever(db,reciever) == False:
        printLines()
        print("Recievers user doesn't exists")
    
    else:
        printLines()
        print("Sender user and Reciever user doesn't exist")