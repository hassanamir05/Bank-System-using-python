from Module3 import *
from Module1 import *
from Module2 import *

def main():

    confirm='y'
    while confirm=='y':
        print("\n\n")
        print("-------------- Welcome --------------")
        print("-------------Main Menu-------------")
        print("1.User Managment\n2.Employee Managment\n3.Employes Accounts in Bank")
        choice=eval(input("Enter Your Choice : "))
        print("\n\n")
        if choice==1:
            while True:
                print("-------------- User Managment --------------")
                print("What do you want to do :\n1.Create an Account\n2.View Account "
                      "Details\n3.Search\n4.Update Account\n5.Exit")
                choice = eval(input("Enter Your Choice : "))
                print()
                if choice <= 5 and choice != 0:
                    if choice == 1:
                        create_user()
                    elif choice == 2:
                        view_user()
                    elif choice == 3:
                        search_user()
                    elif choice == 4:
                        update_user()
                    else:
                        break
                else:
                    print("Invalid Choice!")
        elif choice==2:

            while True:
                print("-------------- Employee Managment --------------")
                print("What do you want to do :\n1.Add an employee\n2.View Employee Details"
                      "\n3.Search Employee \n4.Update Employee Details\n5.Exit")
                choice = eval(input("Enter Your Choice : "))
                print()
                if choice <= 5 and choice != 0:
                    if choice == 1:
                        create_employe()
                    elif choice == 2:
                        view_employe()
                    elif choice == 3:
                        search_employe()
                    elif choice == 4:
                        update_employe()
                    else:
                        break
                else:
                    print("Invalid Choice!")
        elif choice==3:
            details()
        else:
            print("Enter Valid Choice!")

        confirm = input("Press y to use again and any other key to exit : ")
        print()

print("______________________________________________________________________________________________")



main()
