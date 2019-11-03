import click
# import enchant
from spellchecker import spellchecker as sc
from typing import IO
from tqdm import tqdm

from cypher import encrypt


@click.command()
@click.option(
    '--input_file',
    type=click.File('r'),
    required=True,
)
@click.option(
    '--output_file',
    '-o',
    default='crackedtext.txt',
    type=click.File('w'),
    required=True,
)
def breakit(input_file: IO[str], output_file: IO[str]) -> IO[str]:
    """
    Brute force breaker to crack encrypted text.

    Examples:
    $ python breaker.py file_to_crack.txt -o output_file_name.txt
    """
    click.echo('Decoding...')
    encrypted_text = input_file.read()
    # load an English dictionary
    english_dictionary = sc.SpellChecker("en")
    max_number_of_english_words = 0
    # tries possible alphabet shifts and shows a progress bar
    for key in tqdm(range(26)):
        plaintext = encrypt(encrypted_text, -key)
        number_of_english_words = 0

        for word in plaintext.split(' '):
            # check in the word_frequency list of words from the dictionary
            if word in english_dictionary.word_frequency:
                number_of_english_words += 1

        if number_of_english_words > max_number_of_english_words:
            max_number_of_english_words = number_of_english_words
            best_plaintext = plaintext
            best_key = key

    click.echo(
        f'Completed. The most likely encryption key is {best_key}. \
        \nIt gives the following plaintext:\n{best_plaintext[:1000]}...\n'
        )
    output_file.write(best_plaintext)


if __name__ == '__main__':
    breakit()
