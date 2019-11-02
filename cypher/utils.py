import typing
from typing import IO

def encrypt(text: IO[str], key: int) -> str:
    """
    Encrypts a text using shift encryption.
    
    >>> encrypt("Encryption test", 2)
    'Gpetarvkqp vguv'
    >>> encrypt("Encryption test", 4)
    'Irgvctxmsr xiwx'
    """
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            num = ord(char)
            num += key 
            if char.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif char.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    number += 26
            char = chr(num)
        encrypted_text += char
    return encrypted_text

