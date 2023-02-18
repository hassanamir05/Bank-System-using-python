user_registered = 0
user_data=[]

def create_user():
    global user_registered
    name=input("Enter your name : ")
    user_data.append(name)
    cnic=input("Enter your CNIC number : ")
    user_data.append(cnic)
    contact=input("Enter Contact : ")
    user_data.append(contact)
    address = input("Enter the Address : ")
    user_data.append(address)
    user_registered = user_registered + 1
    print("Your account number is ", user_registered)
    print("Account Created Succesfully! ")
    print()
    print()

def view_user():
    global user_registered
    if user_registered!=0:
        print("  ",format("Account Holder Name", "<25s"), format("Account Holder CNIC", "<25s"),
              format("Contact Number   ", "<25s"),format("Account Holder Address", "<25s"))
        print(" ______________________________________________________________________________________________________")
        for i in range(0, len(user_data), 4):
            print("  ", format(user_data[i], "<25s"), format(user_data[i + 1], "<25s")
                  , format(user_data[i + 2], "<25s"), format(user_data[i + 3], "<25s"))
    elif user_registered==0:
        print("No Account Created!")
        print()
    print()

def search_user():
    global user_registered
    temp_accnum = eval(input("Enter your account number : "))
    if ((temp_accnum * 4) <= len(user_data)):
        i=(temp_accnum-1)*4
        print("  ", format("Account Holder Name", "<25s"), format("Account Holder CNIC", "<25s"),
              format("Contact Number", "<25s"), format("Account Holder Address", "<25s"))
        print(" ______________________________________________________________________________________________________")
        if user_registered!=0:
            print("  ", format(user_data[i], "<25s"), format(user_data[i + 1], "<25s")
                  , format(user_data[i + 2], "<25s"), format(user_data[i + 3], "<25s"))
    else:
        print("No Record Found!")

    print("\n")

def update_user():
    global user_registered
    print("What do you want to update :\n1.Account Holder Name\n2.Account Holder CNIC\n3.Account Balance\n4.Address")
    choice=eval(input("Enter your choice : "))
    if choice<=4 and choice!=0:
        temp_accnum = eval(input("Enter your account number : "))
        i = (temp_accnum - 1)*4
        if user_registered!=0:
            if ((temp_accnum * 4) <= len(user_data)):
                if choice == 1:
                    name=input("Enter Your Name : ")
                    user_data[i]=name
                elif choice == 2:
                    cnic=input("Enter Your CNIC number : ")
                    user_data[i + 1]=cnic
                elif choice==3 :
                    contact=input("Enter Account Balance : ")
                    user_data[i + 2]=contact
                else:
                    address = input("Enter your Address : ")
                    user_data[i + 3] = address
            else:
                print("No Record Found!")
        elif user_registered==0:
            print("No Account Created!")
    else:
        print("Invalid Choice!")
    print()
