import numpy as np

# Tamanho do alfabeto considerado
alphabetic_length = 26

# Transforma a letra em um valor numérico
def letter_to_value(letra):
    if len(letra) != 1 or not letra.isalpha():
        raise ValueError("A entrada deve ser uma única letra.")

    # Certifique-se de que a letra seja maiúscula
    letra = letra.upper() 
    # Valor de 'A' é 1, 'B' é 2, e assim por diante
    valor = ord(letra) - ord('A') + 1  
    return valor

# Transforma o texto em uma sequência de valores numéricos
def word_to_values(word, key):
    numbers = []
    for index_letter, letter in enumerate(word):
        if(index_letter % key.shape[0] == 0):
            numbers.append([])
        numbers[-1].append(letter_to_value(letter))

    return np.array(numbers).transpose()

# Realiza o resto da divisão de acordo com o tamanho do alfabeto
def mod_alphabetic_length(number):
    return number % alphabetic_length

# Realiza a multiplicação de matrizes e o resto da divisão de acordo
def hill_operation(matrix1, matrix2):

    multiplication_matrix = []

    if(matrix1.shape[1] == matrix2.shape[0]):
        multiplication_matrix = np.dot(matrix1, matrix2)

        for i in range(multiplication_matrix.shape[0]):
            for j in range(multiplication_matrix.shape[1]):

                item = multiplication_matrix[i, j]

                value = mod_alphabetic_length(item)
                if(value == 0):
                    value = alphabetic_length
                
                multiplication_matrix[i, j] = value

    multiplication_matrix_rounded = np.round(multiplication_matrix).astype(int)
    return np.array(multiplication_matrix_rounded).transpose()
    
# Transforma valor numérico em letra
def value_to_letter(value):
    if not isinstance(value, int) or value < 1 or value > alphabetic_length:
        raise ValueError(f"O valor deve ser um número entre 1 e {alphabetic_length}.")

    # 'A' é 1, 'B' é 2, e assim por diante
    letra = chr(value + ord('A') - 1)
    return letra

# Transforma valores numéricos em texto
def values_to_word(values):
    values_list = np.concatenate(values).tolist()

    array_letters = []
    for number in values_list:
        letter = value_to_letter(number)
        array_letters.append(letter)

    cripted_message = ''.join(array_letters)

    return cripted_message

# Criptografia usando cifra de Hill
def hillCipherCrypt(text, key):

    # Tenho o valor da chave
    print(f"Chave:")
    print(key)

    # Tenho o texto claro
    print(f"Texto claro: {text}")

    # Converto o texto em uma matriz com valores numéricos
    text_in_matrix = word_to_values(text, key)
    print(f"Matriz do texto claro:")
    print(text_in_matrix)

    # Realizo a multiplicação aplicando a chave
    cripted_text_in_matrix = hill_operation(key, text_in_matrix)
    print(f"Matriz do texto cifrado:")
    print(cripted_text_in_matrix)

    # Converto os valores numéricos da matriz anterior em texto novamente
    cripted_message = values_to_word(cripted_text_in_matrix)
    print(f"Texto criptografado: {cripted_message}")

    # Texto cifrado
    return cripted_message

# Descriptografia usando cifra de Hill
def hillCipherDecrypt(text, key):

    # Obtenho a matriz inversa da chave original 
    key_numpy = np.array(key)
    key_decryption = np.linalg.inv(key_numpy)
    print(f"Chave para descriptografar:")
    print(key_decryption)

    # Tenho o texto cifrado
    print(f"Texto cifrado: {text}")

    # Converto o texto em uma matriz com valores numéricos
    text_in_matrix = word_to_values(text, key_decryption)
    print(f"Matriz do texto cifrado:")
    print(text_in_matrix)

    # Realizo a multiplicação aplicando a chave
    decripted_text_in_matrix = hill_operation(key_decryption, text_in_matrix)
    print(f"Matriz do texto claro:")
    print(decripted_text_in_matrix)

    # Converto os valores numéricos da matriz anterior em texto novamente
    decripted_message = values_to_word(decripted_text_in_matrix)
    print(f"Texto descriptografado: {decripted_message}")

    # Texto claro
    return decripted_message