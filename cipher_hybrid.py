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
