#PLAYFAIR
def create_playfair_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J is excluded
    matrix = []
    key = "".join(dict.fromkeys(key.upper().replace("J", "I") + alphabet))  # Unique characters
    for i in range(0, 25, 5):
        matrix.append(list(key[i:i+5]))
    return matrix

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col

def playfair_encrypt(plaintext, key):
    matrix = create_playfair_matrix(key)
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    if len(plaintext) % 2 != 0:
        plaintext += "X"  # Padding for odd length

    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i + 1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    return ciphertext

# Example usage
plaintext = "NAMASTHE"
key = "TWOHANDS"
print("Encrypted:", playfair_encrypt(plaintext, key))


#CAESERCIPHER
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# Example usage
text = "NEURALNETWORKS"
shift = 3
print("Encrypted:", caesar_cipher(text, shift))



#HILLCIPHER
import numpy as np

def hill_cipher_encrypt(plaintext, key_matrix):
    n = len(key_matrix)
    plaintext = plaintext.upper().replace("", "")
    if len(plaintext) % n != 0:
        plaintext += "X" * (n - len(plaintext) % n)

    plaintext_vector = [ord(char) - ord('A') for char in plaintext]
    ciphertext = ""

    for i in range(0, len(plaintext_vector), n):
        block = plaintext_vector[i:i+n]
        result = np.dot(key_matrix, block) % 26
        ciphertext += "".join(chr(num + ord('A')) for num in result)

    return ciphertext

plaintext = "REUSABLEROCKETS"
key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
print("encrypted:", hill_cipher_encrypt(plaintext, key_matrix))



# Function for Vigenère Cipher Encryption
def vigenere_encrypt(plaintext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key.upper()
    plaintext = plaintext.upper().replace(" ", "")
    cipher_text = ""
    key_index = 0
    
    for char in plaintext:
        if char in alphabet:
            shift = alphabet.index(key[key_index % len(key)])
            cipher_text += alphabet[(alphabet.index(char) + shift) % len(alphabet)]
            key_index += 1
        else:
            cipher_text += char
    
    return cipher_text

# Function for Vigenère Cipher Decryption
def vigenere_decrypt(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key.upper()
    ciphertext = ciphertext.upper().replace(" ", "")
    plain_text = ""
    key_index = 0
    
    for char in ciphertext:
        if char in alphabet:
            shift = alphabet.index(key[key_index % len(key)])
            plain_text += alphabet[(alphabet.index(char) - shift) % len(alphabet)]
            key_index += 1
        else:
            plain_text += char
    
    return plain_text

# Function for Columnar Transposition Cipher Encryption
def columnar_transposition_encrypt(plaintext, key):
    num_cols = len(key)
    num_rows = len(plaintext) // num_cols + (1 if len(plaintext) % num_cols else 0)
    
    grid = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    for i, char in enumerate(plaintext):
        row = i // num_cols
        col = i % num_cols
        grid[row][col] = char
    
    key_order = sorted(range(len(key)), key=lambda x: key[x])
    ciphertext = ''.join(''.join(grid[row][col] for row in range(num_rows) if grid[row][col] != '') for col in key_order)
    
    return ciphertext

# Function for Columnar Transposition Cipher Decryption
def columnar_transposition_decrypt(ciphertext, key):
    num_cols = len(key)
    num_rows = len(ciphertext) // num_cols
    
    key_order = sorted(range(len(key)), key=lambda x: key[x])
    grid = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    
    idx = 0
    for col in key_order:
        for row in range(num_rows):
            if idx < len(ciphertext):
                grid[row][col] = ciphertext[idx]
                idx += 1
    
    plaintext = ''.join(''.join(grid[row][col] for col in range(num_cols)) for row in range(num_rows))
    return plaintext.strip()

# Full Hybrid Encryption Function
def hybrid_encrypt(plaintext, vigenere_key, columnar_key):
    vigenere_encrypted = vigenere_encrypt(plaintext, vigenere_key)
    columnar_encrypted = columnar_transposition_encrypt(vigenere_encrypted, columnar_key)
    return columnar_encrypted

# Full Hybrid Decryption Function
def hybrid_decrypt(ciphertext, vigenere_key, columnar_key):
    columnar_decrypted = columnar_transposition_decrypt(ciphertext, columnar_key)
    vigenere_decrypted = vigenere_decrypt(columnar_decrypted, vigenere_key)
    return vigenere_decrypted

# Example usage
plaintext = "HELLO WORLD"
vigenere_key = "KEY"
columnar_key = "SECRET"

# Encryption
encrypted_text = hybrid_encrypt(plaintext, vigenere_key, columnar_key)
print(f"Encrypted Text: {encrypted_text}")

# Decryption
decrypted_text = hybrid_decrypt(encrypted_text, vigenere_key, columnar_key)
print(f"Decrypted Text: {decrypted_text}")
