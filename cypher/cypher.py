import click
from typing import IO, Optional
from utils import encrypt


@click.command()
@click.option(
    '--input_file',
    type=click.File('r'),
    help='File in which there is the text you want to encrypt/decrypt.'
         'If not provided, a prompt will allow you to type the input text.',
)
@click.option(
    '--output_file',
    '-o',
    type=click.File('w'),
    default='cyphertext.txt',
    show_default=True,
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
def cypher(
           input_file: Optional[IO[str]],
           output_file: Optional[IO[str]],
           decrypt: Optional[str],
           key: Optional[int]
          ) -> None:
    """
    Runs text encryption from the command line.

    Examples:
    $ python cypher.py
    $ python cypher.py -e -o output_file_name.txt
    $ python cypher.py -e -k 2
    $ python cypher.py -d file_to_decrypt.txt -o output_file_name.txt -k 2
    """
    if input_file:
        text = input_file.read()
    else:
        text = click.prompt(
                            'Enter a text',
                            hide_input=not decrypt
                           )
    if decrypt:
        key = -key

    cyphertext = encrypt(text, key)

    if output_file:
        # saves a .txt file in directory
        output_file.write(cyphertext)
    else:
        click.echo(cyphertext)


if __name__ == '__main__':
    cypher()
