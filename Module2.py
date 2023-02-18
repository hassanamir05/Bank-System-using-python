total_employe = 0
employe_data=[]

def create_employe():
    global total_employe
    name=input("Enter your name : ")
    employe_data.append(name)
    cnic=input("Enter your CNIC number : ")
    employe_data.append(cnic)
    contact_=input("Enter Contact : ")
    employe_data.append(contact_)
    address = input("Enter the Address : ")
    employe_data.append(address)
    total_employe = total_employe + 1
    print("Your ID is ", total_employe)
    print()
    print()
def view_employe():
    global total_employe
    if total_employe != 0:
        print("  ", format("Employe Name   ", "<25s"), format("Employe CNIC   ", "<25s"),
              format("Employe Contact Number  ", "<25s"), format("Employe Address   ", "<25s"))
        print(" ______________________________________________________________________________________________________")
        for i in range(0, len(employe_data), 4):
            print("  ", format(employe_data[i], "<25s"), format(employe_data[i + 1], "<25s")
                  , format(employe_data[i + 2], "<25s"), format(employe_data[i + 3], "<25s"))
    elif total_employe == 0:
        print("No Employe!")
        print()
    print()

def search_employe():
    global total_employe
    temp_id = eval(input("Enter your ID : "))
    if ((temp_id * 4) <= len(employe_data)):
        i = (temp_id - 1) * 4
        print("  ", format("Employe Name   ", "<25s"), format("Employe CNIC   ", "<25s"),
              format("Employe Balance   ", "<25s"), format("Employe Address   ", "<25s"))
        print(" ______________________________________________________________________________________________________")
        if employe_data != 0:
            print("  ", format(employe_data[i], "<25s"), format(employe_data[i + 1], "<25s")
                  , format(employe_data[i + 2], "<25s"), format(employe_data[i + 3], "<25s"))
    else:
        print("No Record Found!")

    print("\n\n")

def update_employe():
    global total_employe
    print("What do you want to update :\n1.Employe Name\n2.Employe CNIC\n3.Employe Contact Number\n4.Employe Address")
    choice = eval(input("Enter your choice : "))
    if choice <= 4 and choice != 0:
        temp_accnum = eval(input("Enter your ID : "))
        i = (temp_accnum - 1) * 4
        if total_employe != 0:
            if ((temp_accnum * 4) <= len(employe_data)):
                if choice == 1:
                    name = input("Enter Your Name : ")
                    employe_data[i] = name
                elif choice == 2:
                    cnic = input("Enter Your CNIC number : ")
                    employe_data[i + 1] = cnic
                elif choice==3:
                    balance = input("Enter Contact Number : ")
                    employe_data[i + 2] = balance
                else:
                    address=input("Enter your Address : ")
                    employe_data[i + 3] = address
            else:
                print("No Record Found!")
        elif total_employe == 0:
            print("No Employe!")
    else:
        print("Invalid Choice!")
    print()
