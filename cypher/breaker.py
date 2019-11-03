import click
import enchant
import typing
from typing import IO

from cypher import encrypt

@click.command()
@click.option(
    '--text',
    type=click.File('r'),
    required=True,
)
@click.option(
    '--output_write',
    '-o',
    type=click.File('w'),
    required=True,
)
def breakit(text: IO[str], output_write: IO[str]) -> IO[str]:
    """
    Brute force breaker for encrypted text.
    """
    encrypted_text = text.read()
    english_dictionary = enchant.Dict("en_US")
    max_number_of_english_words = 0

    for key in range(26):
        plaintext = encrypt(encrypted_text, -key)
        number_of_english_words = 0

        for word in plaintext.split(' '):
            if word and english_dictionary.check(word):
                number_of_english_words += 1

        if number_of_english_words > max_number_of_english_words:
            max_number_of_english_words = number_of_english_words
            best_plaintext = plaintext
            best_key = key

    click.echo(f'The most likely encryption key is {best_key}. \
        \nIt gives the following plaintext:\n{best_plaintext[:1000]}...\n')
    output_write.write(best_plaintext)

if __name__ == '__main__':
    breakit()