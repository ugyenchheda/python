

master_pwd = input("What is the master password? ")


def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            #print(line.rstrip())
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:",user, "Password:", passw)

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("passwords.txt", 'a') as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode = input("Would you like to add a new password or view existing one?(View/add) ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()

    else:
        print ("Invalid option.")
        continue