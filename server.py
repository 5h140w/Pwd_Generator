from functions.password_generator import generate_password
from functions.pwd import PWD
import sys


if __name__=="__main__":
    if(len(sys.argv)==1):
        print(generate_password())
    else:
        print(PWD(int(sys.argv[1])))