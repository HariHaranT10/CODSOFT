from os import system

global contacts
contacts = {}


def new_contact():

    global contacts

    while True:
        print("\nPlease enter the following details: ")
        name = input("Name: ")
        address = input("Address: ")
        phone = input(" Phone number: ")



        details = {'address': address,
                   'phone': phone,}

        contacts[name] = details
        print("\nContact details saved successfully \N{check mark}")

        if input("Do you want to add another contact (y/n) ?: ").lower() != 'y': break


def del_contact():
    ''' Input ==> Contact Name (to be deleted) '''

    global contacts

    if contacts == {}:
        print(
            "You don't have any contacts saved! Consider adding a few new contacts.")
    else:
        while True:

            print("\n-------- Your Contacts --------")
            for item in contacts:
                print(f'> {item}')

            name_del = input(
                "\nEnter the name of the Contact you want to delete\n[Write 'DEL_ALL' to delete all of your existing contacts]: ")

            if name_del == 'DEL_ALL':
                del_choice = input(
                    "\nYou are about to delete all of your contacts after this command, if you really wish to, write \"CONFIRM\":\n")
                if del_choice == "CONFIRM":
                    contacts.clear()
                    print("All of your contacts were deleted successfully \N{check mark}")
                else:
                    print('User\'s contacts were not deleted')

                if input("Do you want to delete another contact (y/n) ?: ").lower() != 'y': break
                if contacts == {}:
                    print("You don't have any contacts saved! Consider adding a few new contacts.")
                    break

            elif name_del in contacts:
                del contacts[name_del]
                print("\nContact deleted \N{check mark}")

                if input("Do you want to delete another contact (y/n) ?: ").lower() != 'y': break
                if contacts == {}:
                    print("You don't have any contacts saved! Consider adding a few new contacts.")
                    break
            else:
                print("The Contact name entered does not exit.")


def edit_contact():


    global contacts

    if contacts == {}:
        print("You don't have any contacts saved! Consider adding a few new contacts.")
    else:
        while True:
            print("\n-------- Your Contacts--------")
            for item in contacts.keys():
                print(f'> {item}')

            name_edit = input("\nEnter the name of the Contact you want to edit: ")

            if name_edit in contacts:
                print("-------- Contact Details --------")
                print(f"> {name_edit}")
                for item in contacts[name_edit]:
                    print(f"> {contacts[name_edit][item]}")

                print(
                    "\nPlease write the attribute you want to change, and the new data in the below mentioned format :-\n\n\t\t\t\t\t<attribute>|<editted_info>")
                print("\nFollowing are the attributes you can edit:\n\n|--address--|\n|---phone---|\n|---email---|\n")
                user_edit = input('\n').split('|')

                contacts[name_edit][user_edit[0]] = user_edit[
                    1]
                print("\nContact details updated successfully \N{check mark}")

                if input("Do you want to update your contacts again (y/n) ?: ").lower() != 'y': break
            else:
                print("\nThe Contact name entered does not exit.")


def view_details():
    global contacts

    if contacts == {}:
        print("You don't have any contacts saved! Consider adding a few new contacts.")
    else:
        while True:
            print("-------- Your Contacts --------")
            for item in contacts.keys():
                print(f"> {item}")

            name_info = input("\nEnter the name of the Contact whose details you wish to view: ")

            if name_info in contacts:
                print(f"\n---- Contact Details for {name_info} ----")
                for item in contacts[name_info]:
                    print(f">> {contacts[name_info][item]}")

                if input("Do you wish to view your contacts again (y/n) ?: ").lower() != 'y': break
            else:
                print("\nThe Contact name entered does not exist")


def contactBook():
    while True:
        system('cls')
        print("========== CONTACT BOOK ========== ")
        print(
            "Enter: \n[1] to add a New Contact\n[2] to view your Contacts\n[3] to edit a Previously Existing Contact\n[4] to delete a Previously Existing Contact")

        choice = int(input("\nEnter your choice: "))

        if choice in (1, 2, 3,4):
            if choice == 1:
                new_contact()
            elif choice == 2:
                view_details()
            elif choice == 3:
                edit_contact()
            else:
                del_contact()
        else:
            print("Invalid Choice. Please Try Again.")

        if input("\nDo you want to open your Contact Book again (y/n) ?: ").lower() != 'y':
            break


contactBook()
