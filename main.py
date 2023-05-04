from encryption_functions import hash_function, encrypt_string, decrypt_string, copy2clip, replace_passkey, get_encryption_line
import os

def set_encryption_key():
    input_encryption_line = input("Enter a key to encrypt your data: ")
    input_passkey = input("Enter a passkey (this will be asked every time you use the program): ")

    new_keyword = encrypt_string(input_encryption_line, input_passkey)

    print(input_encryption_line, input_passkey)
    replace_passkey(new_keyword)
    print("Passkey changed to: ", get_encryption_line(input_passkey))


def welcome_message():
    print("Welcome to the Password Generetor App made by github.com/xa-m\n")
    print("How to use? -> https://github.com/xa-m/Python_Password_Generetor\n")
    print("Type following to access features:")
    print("    1. Generate password (default)")
    print("    2. Replace or Create new encryption key and passcode")
    print("    3. Get your old encryption key\n")


def experimental_main():
    print("If you are setting up a new passkey then type 'new'")
    user_input_passkey = input("Enter your passkey: ")
    if user_input_passkey == "new":
        set_encryption_key()
        return # it will be continue when the main function changed to a loop
    
    encryption_line = get_encryption_line(user_input_passkey)
    if encryption_line == None:
        print("Incorrect passkey")
        return # it will be continue when the main function changed to a loop
    
    print("Your encryption line is: ", encryption_line)
    
    user_keyword_input = input("Enter your keyword: ")
    encrypted_password = hash_function(encryption_line, user_keyword_input)
    print("Your password is: ", encrypted_password)
    copy2clip(encrypted_password)

def generete_password_gui():
    print("You are creating new password, first you have to put your passkey to access your encryption key.")
    while(True):
        user_input_passkey = input("Enter your passkey: ")
        encryption_line = get_encryption_line(user_input_passkey)
        if encryption_line == None:
            print("Incorrect passkey\n")
            continue
        else:
            break
    
    # print("Your encryption line is: ", encryption_line) #! DEBUG (DO NOT INCLUDE IN PRODUCTION)
    
    print("\nAfter you have your encryption key, you need to enter a service name for your password")
    
    user_input_service_name = input("Enter your service name: ")

    encrypted_password = hash_function(encryption_line, user_input_service_name)
    copy2clip(encrypted_password)
    print("Your password is: ", encrypted_password + " (copied to clipboard)")
    

def generate_new_encryption_key_gui():
    print("If you used this app before, you need to use your old encryption key to access your old passwords. You'll need to enter two parameters.")
    print("   1. Your encryption line which has to be a secret and the main key.")
    print("   2. The passcode which will be asked every time you use the program. (does not effect the passwords)\n")

    user_input_encryption_line = input("Enter your encryption line: ")
    user_input_passcode = input("Enter your passcode for the App: ")

    encrypted_encryption_line = encrypt_string(user_input_encryption_line, user_input_passcode)
    replace_passkey(encrypted_encryption_line)

    print("Your new encryption line is: ", user_input_encryption_line)
    print("Your new passcode is: ", user_input_passcode)


def get_old_encryption_key_gui():
    print("Seems like you want to get your encryption key, you'll need to have your passkey to access your encryption key.")
    while(True):
        user_input_passkey = input("Enter your passkey: ")
        encryption_line = get_encryption_line(user_input_passkey)
        if encryption_line == None:
            print("Incorrect passkey\n")
            continue
        else:
            break
    
    print("\nYour encryption line is: ", encryption_line)


def main():
    while(True):
        os.system("cls")
        welcome_message()
        user_answer = input("Enter your choice: ")
        os.system("cls")
        if user_answer == "1":
            generete_password_gui()
            break
        elif user_answer == "2":
            generate_new_encryption_key_gui()
            continue
        elif user_answer == "3":
            get_old_encryption_key_gui()
            break



if __name__ == "__main__":
    main()