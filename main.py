from Module3 import *
from Module1 import *
from Module2 import *
def main():
    confirm='y'
    while confirm=='y':
        print("\n\n")
        print("-------------- Welcome --------------")
        print("-------------Main Menu-------------")
        print("1.Current Accounts\n2.Saving Accounts\n3.Combined Account Details")
        choice=eval(input("Enter Your Choice : "))
        print("\n\n")
        if choice==1:
            while True:
                print("-------------- Current Account --------------")
                print("What do you want to do :\n1.Create an Account\n2.View Account "
                      "Details\n3.Search\n4.Update Account\n5.Exit")
                choice = eval(input("Enter Your Choice : "))
                print()
                if choice <= 5 and choice != 0:
                    if choice == 1:
                        create_acount_current()
                    elif choice == 2:
                        view_current()
                    elif choice == 3:
                        search_current()
                    elif choice == 4:
                        update_curent()
                    else:
                        break
                else:
                    print("Invalid Choice!")
        elif choice==2:

            while True:
                print("-------------- Saving Account --------------")
                print("What do you want to do :\n1.Create an Account\n2.View Account "
                      "Details\n3.Search\n4.Update Account\n5.Exit")
                choice = eval(input("Enter Your Choice : "))
                print()
                if choice <= 5 and choice != 0:
                    if choice == 1:
                        create_acount_saving()
                    elif choice == 2:
                        view_saving()
                    elif choice == 3:
                        search_saving()
                    elif choice == 4:
                        update_saving()
                    else:
                        break
                else:
                    print("Invalid Choice!")
        elif choice==3:
            details()
        else:
            print("Enter Valid Choice!")

        confirm = input("Do you want to Continue ? (y/n) : ")

print("______________________________________________________________________________________________")

main()
