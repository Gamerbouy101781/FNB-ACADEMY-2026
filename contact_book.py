list = [{'name': 'Mhluri', 'phone': '0604936532', 'email': 'mhluribaloyi69@gmail.com'}]
contacts = {}

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    print("============================")
    contact = {'name': f'{name}', 'phone': f'{phone}', 'email': f'{email}' }
    contacts.copy()
    list.append(contact)

def search_contact(name):
    for contacts in list:
        if contacts["name"] == name:
            print(contacts)

def delete_contact(name):
    for contacts in list:
        if contacts["name"] == name:
            del contacts[name]
            print(contacts)



def view_all():
    print(list)

print("============================")
print("1. Add contact")
print("2. Search contact")
print("3. Delete contact")
print("4. View all contact")
print("5. Exit")
print("============================")
option = input("Choose: ")
print("============================")

while option == "1":
    add_contact()
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. View all contact")
    print("5. Exit")
    option = input("Choose: ")
while option == "2":
    search_contact(name=input("Search: "))
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. View all contact")
    print("5. Exit")
    option = input("Choose: ")
while option == "3":
    delete_contact(name=input("Delete: "))
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. View all contact")
    print("5. Exit")
    option = input("Choose: ")
    while option == "1":
        add_contact()
        print("1. Add contact")
        print("2. Search contact")
        print("3. Delete contact")
        print("4. View all contact")
        print("5. Exit")
    while option == "2":
        search_contact(name=input("Search: "))
        print("1. Add contact")
        print("2. Search contact")
        print("3. Delete contact")
        print("4. View all contact")
        print("5. Exit")
    while option == "3":
        delete_contact(name=input("Delete: "))
        print("1. Add contact")
        print("2. Search contact")
        print("3. Delete contact")
        print("4. View all contact")
        print("5. Exit")
    while option == "4":
        view_all()
        print("1. Add contact")
        print("2. Search contact")
        print("3. Delete contact")
        print("4. View all contact")
        print("5. Exit")
    while option == "5":
        break


while option == "4":
    view_all()
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. View all contact")
    print("5. Exit")
    option = input("Choose: ")
    while option == "1":
        add_contact()
        print("1. Add contact")
        print("2. Search contact")
        print("3. Delete contact")
        print("4. View all contact")
        print("5. Exit")
    while option == "2":
        search_contact(name=input("Search: "))
        print("1. Add contact")
        print("2. Search contact")
        print("3. Delete contact")
        print("4. View all contact")
        print("5. Exit")
    while option == "3":
        delete_contact(name=input("Delete: "))
        print("1. Add contact")
        print("2. Search contact")
        print("3. Delete contact")
        print("4. View all contact")
        print("5. Exit")
    while option == "4":
        view_all()
        print("1. Add contact")
        print("2. Search contact")
        print("3. Delete contact")
        print("4. View all contact")
        print("5. Exit")
    while option == "5":
        break

while option == "5":
    break
   
