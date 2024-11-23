import random

def policy(_, __, bounds: tuple):
    return random.randint(bounds[0], bounds[1])

