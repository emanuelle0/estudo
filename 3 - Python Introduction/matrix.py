users = []
doContinue = True
print("Press 1 to enter.")
userEnter = input()
if userEnter == "1":
    while doContinue:
        print("Insert name: ")
        name = input()
        print("Insert age: ")
        age = input()
        print("Insert document number: ")
        documentNumber = input()
        users.append([name, age, documentNumber])
        print("Press 1 to continue.")
        userEnter = input()
        if userEnter != "1":
            doContinue = False


file = open("matrix.txt", "x")
file.write("----------------------------------------- \n")
file.close()
for i in range(len(users)):
    for j in range(len(users[i])):
        with open("matrix.txt", "a") as file:
            file.write( users[i][j] + "\t | ")
    with open("matrix.txt", "a") as file:
            file.write("\n ----------------------------------------- \n")


    
