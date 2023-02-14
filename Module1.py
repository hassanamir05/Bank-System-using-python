current_account_registered = 0
current_account_data=[]

def create_acount_current():
    global current_account_registered
    name=input("Enter your name : ")
    current_account_data.append(name)
    cnic=input("Enter your CNIC number : ")
    current_account_data.append(cnic)
    balance=input("Enter Balance : ")
    current_account_data.append(balance)
    address = input("Enter the Address : ")
    current_account_data.append(address)
    current_account_registered = current_account_registered+1
    print("Your account number is ", current_account_registered)
    print("Account Created Succesfully! ")
    print()
    print()

def view_current():
    global curret_account_registered
    if current_account_registered!=0:
        print("  ",format("Account Holder Name   ", "<25s"), format("Account Holder CNIC   ", "<25s"),
              format("Account Balance   ", "<25s"),format("Account Holder Address   ", "<25s"))
        print(" ______________________________________________________________________________________________________")
        for i in range(0, len(current_account_data), 4):
            print("  ",format(current_account_data[i], "<25s"), format(current_account_data[i + 1], "<25s")
                  , format(current_account_data[i + 2], "<25s"),format(current_account_data[i + 3], "<25s"))
    elif current_account_registered==0:
        print("No Account Created!")
        print()
    print()

def search_current():
    global current_account_registered
    temp_accnum = eval(input("Enter your account number : "))
    if ((temp_accnum * 4) <= len(current_account_data)):
        i=(temp_accnum-1)*4
        print("  ", format("Account Holder Name   ", "<25s"), format("Account Holder CNIC   ", "<25s"),
              format("Account Balance   ", "<25s"), format("Account Holder Address   ", "<25s"))
        print(" ______________________________________________________________________________________________________")
        if current_account_registered!=0:
            print("  ", format(current_account_data[i], "<25s"), format(current_account_data[i + 1], "<25s")
                  , format(current_account_data[i + 2], "<25s"), format(current_account_data[i + 3], "<25s"))
    else:
        print("No Record Found!")

    print("\n\n")

def update_curent():
    global current_account_registered
    print("What do you want to update :\n1.Account Holder Name\n2.Account Holder CNIC\n3.Account Balance\n4.Address")
    choice=eval(input("Enter your choice : "))
    if choice<=4 and choice!=0:
        temp_accnum = eval(input("Enter your account number : "))
        i = (temp_accnum - 1)*4
        if current_account_registered!=0:
            if ((temp_accnum * 4) <= len(current_account_data)):
                if choice == 1:
                    name=input("Enter Your Name : ")
                    current_account_data[i]=name
                elif choice == 2:
                    cnic=input("Enter Your CNIC number : ")
                    current_account_data[i+1]=cnic
                elif choice==3 :
                    balance=input("Enter Account Balance : ")
                    current_account_data[i+2]=balance
                else:
                    address = input("Enter your Address : ")
                    current_account_data[i + 3] = address
            else:
                print("No Record Found!")
        elif current_account_registered==0:
            print("No Account Created!")
    else:
        print("Invalid Choice!")
    print()

