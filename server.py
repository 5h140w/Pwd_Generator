from functions.password_generator import generate_password
from functions.pwd import PWD
from functions.password_generator import intValidation
import sys

if __name__=="__main__":
    if(len(sys.argv)==1):
        print(generate_password())
    else:
        try:
            x = int(sys.argv[1])
        except ValueError:
            print("this is not a integer")
            print(generate_password())
        else:
            if (x<5):
                print("Min Length is 5")
                print(generate_password())
            else:
                print(PWD(x))