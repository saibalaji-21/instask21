Feistel Cipher Encryption and Decryption

This program implements the Feistel Cipher, a symmetric encryption algorithm. The process involves splitting the input data into two halves and applying multiple rounds of encryption using a key.
Steps:

   The input string is converted to an 8-bit binary representation.
    The binary string is divided into two equal halves: left and right.
    A key is input and converted into binary.
    The Feistel structure is applied:
        The right half is modified using the key, and the result is XORed with the left half.
        The two halves are swapped after each round.
    This process repeats for multiple rounds (typically 1 or more).
    After encryption, the binary result is converted back into a string
    Feistel Cipher Functions

    input():
  Takes user input for the string to be encrypted and the encryption key.
    
    Binary Conversion:
 
  The input string is converted into an 8-bit binary format using the ord() function (which returns the ASCII value of a character) and the format() function to ensure each character is represented by 8 bits.

    Splitting the String:
  The binary string is split into two halves: left and right.

    Feistel Round:
  The function performs a single round of the Feistel cipher:
            The right half of the binary string is combined with the key using an addition operation.
            The result is XORed with the left half to create the new right half.
            The left and right halves are swapped to create new values for the next round.

     Final Output:
   After the Feistel rounds, the final binary string is padded with leading zeros (if necessary) to ensure its length is a multiple of 8 bits.
        The binary string is then converted back to text by grouping every 8 bits and converting each group into the corresponding ASCII character.

   Run this implementation live on Google Colab:https://colab.research.google.com/drive/1Q0JFUI6yM1ouSdsc6MGaA0FouB4Zn5hO?usp=sharing#scrollTo=6vKWCQAobXYg
