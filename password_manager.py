from cryptography.fernet import Fernet  # Importing Fernet for encryption and decryption


# Function to load the encryption key from a file
def load_key():
    file = open("key.key", "rb")  # Open the key file in read-binary mode
    key = file.read()  # Read the key from the file
    file.close()  # Close the file
    return key  # Return the key


# Load the encryption key from the file
key = load_key()
# Create a Fernet encryption instance using the loaded key
fer = Fernet(key)


# Function to view stored passwords
def view():
    with open('passwords.txt', 'r') as f:  # Open the file in read mode
        for line in f.readlines():  # Read all lines from the file
            data = line.rstrip()  # Remove trailing newline characters
            user, passw = data.split("|")  # Split each line at '|'
            
            # Decrypt the stored password and print it
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())


# Function to add a new password
def add():
    name = input('Account Name: ')  # Ask user for account name
    pwd = input("Password: ")  # Ask user for the password

    # Open file in append mode to add new credentials
    with open('passwords.txt', 'a') as f:
        # Encrypt the password before storing it
        encrypted_pwd = fer.encrypt(pwd.encode()).decode()
        
        # Write account name and encrypted password to the file
        f.write(name + "|" + encrypted_pwd + "\n")


# Main loop for user interaction
while True:
    # Ask the user what they want to do
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()

    if mode == "q":  # Exit the loop if user types 'q'
        break

    if mode == "view":  # If user chooses 'view', call the view function
        view()
    elif mode == "add":  # If user chooses 'add', call the add function
        add()
    else:
        print("Invalid mode.")  # Handle invalid inputs
        continue  # Restart the loop
