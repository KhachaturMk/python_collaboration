import csv

def load_data(filename):
    mylist = []
    with open(filename, mode='r', newline='') as Users:
        Users_data = csv.reader(Users, delimiter=',')
        for row in Users_data:
            mylist.append(row)
    return mylist  
