from random import randrange, choice
from string import ascii_letters
import re


def get_unique_short_id():
    rand_string = ''.join(
        choice(ascii_letters) + str(randrange(9)) for i in range(3)
    )
    return rand_string


def char_validator(text):
    if len(text) > 16:
        return False
    return bool(re.match("""^[a-zA-Z0-9]+$""", text))
