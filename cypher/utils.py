from typing import IO


def encrypt(plaintext: IO[str], key: int) -> str:
    """
    Encrypts a text using shift encryption.

    >>> encrypt("Encryption test", 2)
    'Gpetarvkqp vguv'
    >>> encrypt("Encryption test", 4)
    'Irgvctxmsr xiwx'
    """
    cyphertext = ''

    for char in plaintext:
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
                    num += 26

            char = chr(num)
        cyphertext += char

    return cyphertext
