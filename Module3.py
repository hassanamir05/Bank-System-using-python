from Module1 import *
from Module2 import *
common_number=0
def user_account_details():
    global user_data
    if(len(user_data)!=0):
        print("  ", format("Account Holder Name   ", "<25s"), format("Account Holder CNIC   ", "<25s"),
              format("Account Holder Contact   ", "<25s"), format("Account Holder Address   ", "<25s"))
        print(" _____________________________________________________________________________________________________")
        for i in range(0, len(user_data), 4):
            print("  ", format(user_data[i], "<25s"), format(user_data[i + 1], "<25s")
                  , format(user_data[i + 2], "<25s"), format(user_data[i + 3], "<25s"))
    else:
        print("  No Account Created!")
def employe_details():
    global employe_data
    if (len(employe_data)!=0):
        print("  ", format("Employe Name   ", "<25s"), format("Employe CNIC   ", "<25s"),
              format("Employe Contact  ", "<25s"), format("Employe Address   ", "<25s"))
        print(" ______________________________________________________________________________________________________")
        for i in range(0, len(employe_data), 4):
            print("  ", format(employe_data[i], "<25s"), format(employe_data[i + 1], "<25s")
                  , format(employe_data[i + 2], "<25s"), format(employe_data[i + 3], "<25s"))
    else:
        print("  No Account Created!")
    print()

def common():
    global common_number
    print("  ", format("Employe Name   ", "<25s"), format("Employe CNIC   ", "<25s"),
          format("Employee Contact   ", "<25s"), format("Employe Address   ", "<25s"))
    print(" ______________________________________________________________________________________________________")
    for i in range(1, len(user_data), 4):
            for j in range(1, len(employe_data), 4):
                if (user_data[i]==employe_data[j]):
                        print("  ", format(employe_data[j-1], "<25s"), format(employe_data[j], "<25s")
                              , format(employe_data[j + 1], "<25s"), format(employe_data[j + 2], "<25s"))
                        common_number += 1
    if common_number!=0:
        print("\n")
        print(" ______________________________________________________________________________________________________")
        print("\n\n")
    elif common_number==0:
        print("  No Employee has Account in the Bank!")
        print("\n")
        print(" ______________________________________________________________________________________________________")
        print("\n\n")


def details():
    print("Total Users : ", (len(user_data)) // 4)
    print("Total Employees : ", (len(employe_data)) // 4)
    print("\n")
    print(" ------------------------------------------------------------------------------------------------------")
    print("                                               User Managment                                    ")
    print(" -----------------------------------------------------------------------------------------------------")
    user_account_details()
    print("\n\n")
    print(" ------------------------------------------------------------------------------------------------------")
    print("                                              Employee Managent                                      ")
    print(" ------------------------------------------------------------------------------------------------------")
    employe_details()
    print("\n")
    print(" ------------------------------------------------------------------------------------------------------")
    print("                                     Employees that have Account in the Bank                           ")
    print(" ------------------------------------------------------------------------------------------------------")
    common()
