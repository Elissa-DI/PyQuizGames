from cryptography.fernet import Fernet


# Function to generate and write a new encryption key (uncomment if needed)
# def write_key():
#     key = Fernet.generate_key()
#     with open('key.key', 'wb') as keys_file:
#         keys_file.write(key)

# Function to load the encryption key from a file
def load_key():
    with open('key.key', 'rb') as keys_file:
        key = keys_file.read()
    return key


# Load the encryption key
key = load_key()
fer = Fernet(key)


# Function to view stored passwords
def view():
    with open('passwords.txt', 'r') as file:
        for line in file.readlines():
            data = line.rstrip()
            user, passw = data.split('|')
            decrypted_pass = fer.decrypt(passw.encode()).decode()
            print('User:', user, ' Password:', decrypted_pass)


# Function to add a new password
def add():
    name = input('Enter account name: ')
    password = input('Enter password: ')

    # Encrypt the password and convert it to a string
    encrypted_pass = fer.encrypt(password.encode()).decode()

    with open('passwords.txt', 'a') as file:
        file.write(name + " | " + encrypted_pass + "\n")


# Main loop for the password manager
while True:
    mode = input('Would you like to add a new password or view existing ones (view, add) or Q to quit: ').lower()
    if mode == 'q':
        break
    elif mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid mode 😒')
        continue

print('Goodbye!')
