run = True
telephoneList = {}

def addContact(name, telephone) :
    telephoneList[name] = telephone
    print("Contact to {name} added : {telephone}")

searchContact = lambda name : telephoneList.get(name)

def removeContact(name):
    telephoneList.pop(name)

def showAllContacts():
    print("Telephone List\n ----------------------------------------------------\n")
    for i in telephoneList:
        print(f'{i}: {telephoneList[i]}')
    print("\n ----------------------------------------------------\n")

isNotAnOption = lambda value : True if (value != "1" and value != "2" and value != "3" and value != "4") else False

while run:
    print("Telephone List")
    print(''' 
    Select one of the following options:
    1 - Add new contact.
    2 - Search contact by name.
    3 - Remove contact by name.
    4 - Show all contacts.
    5 - Press any other character to leave the app.
    Option:\n
    ''')
    option = input()
    if isNotAnOption(option):
        run = False
    else:
        if option == "1":
            name = input("Insert contact name: ")
            telephone = input("Insert contact telephone: ")
            addContact(name, telephone)
        elif option == "2":
            name = input("Insert contact name: ")
            try:
                contact = searchContact(name)
                print(f'Contact found - {name} : {contact}')
            except:
                print(f'Contact with requested name > {name} not found.')
        elif option == "3":
            name = input("Insert contact name: ")
            try:
                removeContact(name)
                print(f'Conact {name} removed with success.')
            except:
                print('Contact with required name not found.')
        elif option == "4":
            print('Empty list of contacts.') if len(telephoneList) == 0 else showAllContacts()
                
            
            



           
        




