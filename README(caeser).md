# Caesar Cipher in Python

## Overview
The Caesar cipher is a simple substitution cipher that shifts the letters of the alphabet by a fixed amount. It is one of the oldest known encryption techniques, used for secure communication.

This program allows users to encrypt messages using a shift value.

## Code Explanation

### Encrypting the Text

```python
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
text = "HELLO"
shift = 3
print("Encrypted:", caesar_cipher(text, shift))
```
The function caesar_cipher() shifts each letter in the text by a specified shift value.
It preserves uppercase and lowercase letters.
Non-alphabetic characters remain unchanged.



Run on Google Colab:-(https://colab.research.google.com/drive/1Q0JFUI6yM1ouSdsc6MGaA0FouB4Zn5hO?usp=sharing)
