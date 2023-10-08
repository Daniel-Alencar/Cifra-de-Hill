import numpy as np

# Tamanho do alfabeto considerado
alphabetic_length = 26

def letter_to_value(letra):
    if len(letra) != 1 or not letra.isalpha():
        raise ValueError("A entrada deve ser uma única letra.")

    # Certifique-se de que a letra seja maiúscula
    letra = letra.upper() 
    # Valor de 'A' é 1, 'B' é 2, e assim por diante
    valor = ord(letra) - ord('A') + 1  
    return valor

def word_to_values(word, key):
    numbers = []
    for index_letter, letter in enumerate(word):
        if(index_letter % key.shape[0] == 0):
            numbers.append([])
        numbers[-1].append(letter_to_value(letter))

    return np.array(numbers).transpose()

def mod_alphabetic_length(number):
    return number % alphabetic_length

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

    return np.array(multiplication_matrix).transpose()
    
def value_to_letter(value):
    if not isinstance(value, int) or value < 1 or value > alphabetic_length:
        raise ValueError(f"O valor deve ser um número entre 1 e {alphabetic_length}.")

    # 'A' é 1, 'B' é 2, e assim por diante
    letra = chr(value + ord('A') - 1)
    return letra

def values_to_word(values):
    values_list = np.concatenate(values).tolist()

    array_letters = []
    for number in values_list:
        letter = value_to_letter(number)
        array_letters.append(letter)

    cripted_message = ''.join(array_letters)

    return cripted_message

def hillCipherCrypt(text, key):

    print(f"Chave:")
    print(key)

    print(f"Texto claro: {text}")

    text_in_matrix = word_to_values(text, key)
    print(f"Matrizes do texto claro:")
    print(text_in_matrix)

    cripted_text_in_matrix = hill_operation(key, text_in_matrix)
    print(f"Matrizes do texto cifrado:")
    print(cripted_text_in_matrix)

    cripted_message = values_to_word(cripted_text_in_matrix)
    print(f"Texto criptografado: {cripted_message}")
    return cripted_message

def hillCipherDecrypt(text, key):

    key_numpy = np.array(key)
    determinant = np.linalg.det(key_numpy)
    key_decryption = np.linalg.inv(key_numpy) * determinant
    key_decryption = np.array(key_decryption).astype(int)
    print(f"Chave para descriptografar:")
    print(key_decryption)

    print(f"Texto cifrado: {text}")

    text_in_matrix = word_to_values(text, key_decryption)
    print(f"Matrizes do texto cifrado:")
    print(text_in_matrix)

    decripted_text_in_matrix = hill_operation(key_decryption, text_in_matrix) * 3

    for i in range(decripted_text_in_matrix.shape[0]):
        for j in range(decripted_text_in_matrix.shape[1]):

            item = decripted_text_in_matrix[i, j]

            value = mod_alphabetic_length(item)
            if(value == 0):
                value = alphabetic_length
            
            decripted_text_in_matrix[i, j] = value
    decripted_text_in_matrix = decripted_text_in_matrix.astype(int)
    print(f"Matrizes do texto claro:")
    print(decripted_text_in_matrix)

    decripted_message = values_to_word(decripted_text_in_matrix)
    print(f"Texto descriptografado: {decripted_message}")
    return decripted_message