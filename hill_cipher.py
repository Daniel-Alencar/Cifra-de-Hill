from functions import *
from config import *

import sys

# Obtenho os argumentos passados via linha de comando
script_name = sys.argv[0]
arguments = sys.argv[1:]

# Leio o arquivo desejado
try:
    with open(arguments[1], 'r') as file:
        text = file.read()

    # Realizo a criptografia
    if(arguments[0] == '-encrypt'):

        encripted_message = hillCipherCrypt(text, key)

        if(arguments[2] == '-output'):
            with open(arguments[3], 'w') as file:
                file.write(encripted_message)

    # Realizo a descriptografia
    elif(arguments[0] == '-decrypt'):

        decripted_message = hillCipherDecrypt(text, key)

        if(arguments[2] == '-output'):
            with open(arguments[3], 'w') as file:
                file.write(decripted_message)

    # Erro no comando executado
    else:
        print("Comando inválido!")
except Exception as error:
    print("Comando inválido!")
    print(error)
