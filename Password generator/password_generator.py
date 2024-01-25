import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
        password_length = int(input("Enter password length: "))
        random.shuffle(characters)
        password = []
        for x in range(password_length):
                password.append(random.choice(characters))
        
        random.shuffle(password)
        password = "".join(password)
        print(password)

option = input("Do you want to generate a password? (Y/N): ")
if option == "Y":
        generate_random_password()
        
elif option == "N":
        print("Program ended")
        quit()
        
else:
        print("Invalid input")
        quit()