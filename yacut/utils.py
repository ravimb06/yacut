import re
from random import choice, randrange
from string import ascii_letters


def get_unique_short_id():
    rand_string = ''.join(
        choice(ascii_letters) + str(randrange(9)) for i in range(3)
    )
    return rand_string


def char_validator(text):
    if not len(text) <= 16:
        return False
    return bool(re.match("""^[a-zA-Z0-9]+$""", text))
