import re
from random import choice
from string import ascii_letters, digits

REGEXP_FOR_SHORT_ID = '^[a-zA-Z0-9]+$'


def get_unique_short_id():
    rand_string = ''.join(
        choice(ascii_letters) + choice(digits) for i in range(3)
    )
    return rand_string


def char_validator(text):
    if not len(text) <= 16:
        return False
    return bool(re.match(REGEXP_FOR_SHORT_ID, text))
