HYBRID CIPHER :-

Vigenère + Columnar Transposition
This repository implements a hybrid encryption scheme that combines two classical ciphers:

Vigenère Cipher (Substitution): Each character in the plaintext is shifted based on a random keystream.
Columnar Transposition Cipher (Transposition): The substituted text is rearranged by columns based on a transposition key.

How It Works:
Encryption: The plaintext is first encrypted using the Vigenère cipher with a random keystream, followed by encryption with the Columnar Transposition cipher using a key.
Decryption: The ciphertext is decrypted by first reversing the Columnar Transposition, then decrypting the result with the Vigenère cipher using the original keystream.
This hybrid approach provides stronger encryption by combining both substitution and transposition techniques.



    import random
    import string
     import numpy as np

This function decrypts the ciphertext that was encrypted using the Vigenère cipher with the same key.

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


3. Columnar Transposition Cipher Encryption (columnar_transposition_encrypt)
This function encrypts a message using the Columnar Transposition Cipher, which rearranges the characters of the plaintext into a grid and reads them by columns.


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

Explanation:
Input: plaintext (the message to be encrypted), key (the keyword used to determine the column order)
The plaintext is written into a grid with a number of columns equal to the length of the key. If the grid doesn't fill up, empty spaces are left.
The ciphertext is formed by reading the grid column by column in the order determined by the keyword.
Output: The columnar-transposed ciphertext.

# 4. Columnar Transposition Cipher Decryption (columnar_transposition_decrypt)
This function decrypts the message encrypted using the Columnar Transposition Cipher by reversing the transposition process.

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

Explanation:
Input: ciphertext (the encrypted message), key (the same key used for encryption)
The ciphertext is rearranged into a grid based on the number of columns, and the grid is filled by columns in the order determined by the key.
After reconstructing the grid, the plaintext is read row by row.

5. Hybrid Encryption (hybrid_encrypt)
This function applies both the Vigenère Cipher and Columnar Transposition Cipher to encrypt the plaintext message.


       def hybrid_encrypt(plaintext, vigenere_key, columnar_key):
       vigenere_encrypted = vigenere_encrypt(plaintext, vigenere_key)
       columnar_encrypted = columnar_transposition_encrypt(vigenere_encrypted, columnar_key)
       return columnar_encrypted

Explanation:
Input: plaintext (the original message), vigenere_key (key for Vigenère cipher), columnar_key (key for Columnar Transposition cipher)
First, the plaintext is encrypted using the Vigenère cipher.
Then, the Vigenère-encrypted text is passed through the Columnar Transposition cipher to further encrypt the message.

# Hybrid Decryption (hybrid_decrypt)
This function decrypts the message that was encrypted using both the Vigenère Cipher and Columnar Transposition Cipher.


    def hybrid_decrypt(ciphertext, vigenere_key, columnar_key):
    columnar_decrypted = columnar_transposition_decrypt(ciphertext, columnar_key)
    vigenere_decrypted = vigenere_decrypt(columnar_decrypted, vigenere_key)
    return vigenere_decrypted

Explanation:
Input: ciphertext (the encrypted message), vigenere_key (key for Vigenère cipher), columnar_key (key for Columnar Transposition cipher)
First, the ciphertext is decrypted using the Columnar Transposition cipher.
Then, the result is decrypted using the Vigenère cipher to retrieve the original plaintext.
Output: The original plaintext message after decryption.


Conclusion:
This script implements a hybrid encryption technique that first encrypts the message using the Vigenère Cipher and then applies the Columnar Transposition Cipher. The decryption process reverses both steps to retrieve the original message.



- **LiveTest**: [ClickHere!!](https://colab.research.google.com/drive/1HHzXnzaXDig43Ef3Zgej58nCd0z3Ar3O?usp=sharing)

