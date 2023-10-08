from functions import *
from config import *

import sys

script_name = sys.argv[0]
arguments = sys.argv[1:]

with open(arguments[1], 'r') as file:
    text = file.read()

if(arguments[0] == '-encrypt'):

    encripted_message = hillCipherCrypt(text, key)

    if(arguments[2] == '-output'):
        with open(arguments[3], 'w') as file:
            file.write(encripted_message)

elif(arguments[0] == '-decrypt'):

    decripted_message = hillCipherDecrypt(text, key)

    if(arguments[2] == '-output'):
        with open(arguments[3], 'w') as file:
            file.write(decripted_message)
