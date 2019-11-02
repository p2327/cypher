import click
import typing
from typing import IO 
from utils import encrypt

@click.command()
@click.argument('text', nargs=-1)
@click.option('--decrypt/--encrypt', '-d/-e')
@click.option('--key', '-k', default=1)
def cypher(text: IO[str], decrypt: str, key: int) -> None:
    """
    Runs encrypt from the command line.

    Example:
    $ python cypher.py abcde -e -k 2
    """
    text_string = ''.join(text)
    if decrypt:
        key = -key
    encrypted_text = encrypt(text_string, key)
    click.echo(encrypted_text)

if __name__ == '__main__':
    cypher()