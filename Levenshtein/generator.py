import string
import random


def generator(chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(random.randint(1, 6)))
