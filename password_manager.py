pwd = input("What is the master password? ")

def view():
    with open('passwords.txt') as f:
        for line in f.readlines():
            print(line.rstrip())

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    with open('passwords.txt','a') as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode = input("Would you like to add a new password or vie existing ones (view/add): ").lower()
    if mode == 'q':
        break

    if mode == 'view':
        view()
        
    elif mode == 'add':
        add()
        
    else:
        print("Invalid mode.")
        continue