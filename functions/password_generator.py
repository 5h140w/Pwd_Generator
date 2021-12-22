import string
import random

def intValidation(str):
    while True:
        try:
            userInput = int(input(str))       
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput 
             



def generate_password():
    length= intValidation("Password Length: ")
    while length<5:
        print("Min Length is 5")
        length= intValidation("Password Length: ")
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    random.shuffle(characters)
    password=""
    for i in range(length):
        password+=random.choice(characters)
    return password

