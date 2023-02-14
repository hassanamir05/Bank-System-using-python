from Module1 import *
from Module2 import *

def current_account_details():
    global current_account_data
    if(len(current_account_data)!=0):
        print("  ", format("Account Holder Name   ", "<25s"), format("Account Holder CNIC   ", "<25s"),
              format("Account Balance   ", "<25s"), format("Account Holder Address   ", "<25s"))
        print(" _____________________________________________________________________________________________________")
        for i in range(0, len(current_account_data), 4):
            print("  ", format(current_account_data[i], "<25s"), format(current_account_data[i + 1], "<25s")
                  , format(current_account_data[i + 2], "<25s"), format(current_account_data[i + 3], "<25s"))
    else:
        print("No Account Created!")
def saving_account_details():
    global saving_account_data
    if (len(saving_account_data)!=0):
        print("  ", format("Account Holder Name   ", "<25s"), format("Account Holder CNIC   ", "<25s"),
              format("Account Balance   ", "<25s"), format("Account Holder Address   ", "<25s"))
        print(" ______________________________________________________________________________________________________")
        for i in range(0, len(saving_account_data), 4):
            print("  ", format(saving_account_data[i], "<25s"), format(saving_account_data[i + 1], "<25s")
                  , format(saving_account_data[i + 2], "<25s"), format(saving_account_data[i + 3], "<25s"))
    else:
        print("No Account Created!")
    print()

def details():
    print("Total Accounts : ",((len(current_account_data)+len(saving_account_data)))//4)
    print("Current Accounts : ",(len(current_account_data))//4)
    print("Saving Accounts : ",(len(saving_account_data))//4)
    print("\n")
    print(" ------------------------------------------------------------------------------------------------------")
    print("                                               CURRENT ACCOUNT                                    ")
    print(" -----------------------------------------------------------------------------------------------------")
    current_account_details()
    print("\n\n")
    print(" ------------------------------------------------------------------------------------------------------")
    print("                                              SAVING ACCOUNT                                      ")
    print(" ------------------------------------------------------------------------------------------------------")
    saving_account_details()
