Vigenère Cipher Encryption and Decryption

This Python program implements the Vigenère Cipher, a method of encrypting text by shifting each letter of the plaintext based on a corresponding letter in a key. The Vigenère cipher is a form of polyalphabetic substitution that uses a series of Caesar ciphers, with shifts determined by the letters of the key.
Code Overview

    Vigenère Encryption (vignere_encrypt):
This function encrypts the given plaintext using the key provided by the user.
        The key is converted to uppercase to ensure uniformity, and non-alphabetic characters are left unchanged.
        Each letter of the plaintext is shifted by a number determined by the corresponding letter in the key. The shift is calculated based on the position of the letter in the alphabet (e.g., 'A' corresponds to 0, 'B' to 1, etc.).
        The encryption process repeats the key as needed to match the length of the plaintext.

    Vigenère Decryption (vignere_decrypt):
 This function decrypts the ciphertext back into the original plaintext using the same key.
        The process is similar to encryption, but instead of shifting forward in the alphabet, it shifts backward using the same key.

 Main Execution:
        The program prompts the user to input a plaintext (text to be encrypted) and a key (used for encryption and decryption).
        The vignere_encrypt function is called to generate the ciphertext.
        The vignere_decrypt function is called to retrieve the original plaintext from the ciphertext.
        Both the encrypted and decrypted texts are displayed as output.

Functions

    vignere_encrypt(plaintext, key):
  Purpose: Encrypts the plaintext using the Vigenère cipher and the provided key.
        How it works:
            Loops through each character of the plaintext.
            If the character is a letter, it applies a shift based on the corresponding character in the key (key repeats if necessary).
            Non-alphabetic characters are added unchanged to the ciphertext.

    vignere_decrypt(plaintext, key):
Purpose: Decrypts the ciphertext back to the original plaintext using the same key.
        How it works:
            Loops through each character of the ciphertext.
            For each letter, it shifts it backward in the alphabet based on the corresponding character in the key.
            Non-alphabetic characters are directly appended to the ciphertext.

Example Usage

plaintext = input("ENTER THE PLAINTEXT:")
key = input("Enter the key:")
n = vignere_encrypt(plaintext, key)
print("Encrypted:", n)
print("Decrypted:", vignere_decrypt(n, key))
Example Input:

    plaintext: "HELLO WORLD"
    key: "KEY"

Example Output:

    Encrypted: (Encrypted ciphertext based on the key)
    Decrypted: "HELLO WORLD" (The original plaintext)

How the Vigenère Cipher Works:

    Key: The key is repeated to match the length of the plaintext.
 Shift Calculation: Each letter of the plaintext is shifted forward or backward by the corresponding key letter's position in the alphabet.
        For example, if the key is 'KEY' and the plaintext is 'HELLO', the first letter 'H' is shifted by 'K' (10 positions), the second 'E' is shifted by 'E' (4 positions), and so on.
    Modular Arithmetic: The cipher uses modulo 26 to wrap around the alphabet if the shift goes beyond 'Z'.

Run this implementation live on Google Colab:https://colab.research.google.com/drive/1Q0JFUI6yM1ouSdsc6MGaA0FouB4Zn5hO?usp=sharing#scrollTo=6vKWCQAobXYg
