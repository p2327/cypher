import click
import os
import typing
from typing import IO, Optional
from utils import encrypt

@click.command()
@click.option(
    '--text',
    type=click.File('r'),
    help='File in which there is the text you want to encrypt/decrypt.'
         'If not provided, a prompt will allow you to type the input text.',
)
@click.option(
    '--output_write', 
    '-o',
    type=click.File('w'),
    help='File in which the encrypted / decrypted text will be written.'
         'If not provided, the output text will just be printed.',
)
@click.option(
    '--decrypt/--encrypt',
    '-d/-e',
    help='Whether you want to encrypt the input text or decrypt it.'
)
@click.option(
    '--key',
    '-k',
    default=1,
    help='The numeric key to use for encryption / decryption.'
)
def cypher(text: Optional[IO[str]], output_write: Optional[IO[str]],  decrypt: Optional[str], key: int) -> None:
    """
    Runs encrypt from the command line.

    Example:
    $ python cypher.py -e -o -k 2
    """
    if text:
        text = text.read()
    else:
        text = click.prompt('Enter a text', 
        hide_input=not decrypt)
    if decrypt:
        key = -key
    encrypted_text = encrypt(text, key)
    if output_write:
        # saves a .txt file in directory
        output_write.write(encrypted_text)
    else:
        click.echo(encrypted_text)

if __name__ == '__main__':
    cypher()