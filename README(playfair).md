#Playfair Cipher

The Playfair cipher is a classical encryption technique that encrypts pairs of letters using a 5x5 matrix. The matrix is created from a keyword, followed by the remaining letters of the alphabet (excluding 'J', which is combined with 'I').

#Code Explanation:

create_playfair_matrix(key): Generates a 5x5 matrix from the keyword, removing duplicates and filling in with the remaining alphabet.

find_position(matrix, char): Finds the position (row, column) of a character in the matrix.

playfair_encrypt(plaintext, key): Encrypts the plaintext by converting it to pairs and applying the Playfair cipher rules.


#Example:

plaintext = "HELLO"
key = "KEYWORD"
print("Encrypted:", playfair_encrypt(plaintext, key))
This will output the encrypted text for the input message using the Playfair cipher.


#[Run on Google Colab]"(https://colab.research.google.com/drive/1Q0JFUI6yM1ouSdsc6MGaA0FouB4Zn5hO?usp=sharing)" 
