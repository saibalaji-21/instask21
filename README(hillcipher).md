🔐 Hill Cipher Encryption using Python & NumPy
📜 Overview

The Hill Cipher is a polygraphic substitution cipher that uses linear algebra for encryption. It processes plaintext in blocks and encrypts it using matrix multiplication over modular arithmetic (mod 26). This implementation in Python leverages NumPy for fast computations.

🚀 How It Works

1️⃣ Convert plaintext characters to numerical values (A = 0, B = 1, ..., Z = 25).

2️⃣ Divide plaintext into blocks of size n × n (based on the key matrix).

3️⃣ Multiply each block by the key matrix and take modulo 26.

4️⃣ Convert the resulting numbers back to letters to form the ciphertext.

5️⃣ If necessary, the plaintext is padded with "X" to fit the block size.

🖥️ Code Implementation

🔢 Hill Cipher Encryption Algorithm

python

import numpy as np

def hill_cipher_encrypt(plaintext, key_matrix):
    n = len(key_matrix)
    plaintext = plaintext.upper().replace("", "")  # Remove spaces
    if len(plaintext) % n != 0:
        plaintext += "X" * (n - len(plaintext) % n)  # Padding

    plaintext_vector = [ord(char) - ord('A') for char in plaintext]
    ciphertext = ""

    for i in range(0, len(plaintext_vector), n):
        block = plaintext_vector[i:i+n]
        result = np.dot(key_matrix, block) % 26  # Matrix multiplication mod 26
        ciphertext += "".join(chr(num + ord('A')) for num in result)

    return ciphertext

# Example Usage
plaintext = "HELLO"
key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
print("🔐 Encrypted Text:", hill_cipher_encrypt(plaintext, key_matrix))


🔗 Google Colab Notebook

Run this implementation live on Google Colab:https://colab.research.google.com/drive/1Q0JFUI6yM1ouSdsc6MGaA0FouB4Zn5hO?usp=sharing#scrollTo=6vKWCQAobXYg

📌 Hill Cipher Implementation on Google Colab

