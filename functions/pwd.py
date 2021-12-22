import string
import random

def PWD(length):
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    random.shuffle(characters)
    password=""
    for i in range(length):
        password+=random.choice(characters)
    return password
    