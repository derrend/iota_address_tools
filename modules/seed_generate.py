#!/usr/bin/python3
# Builtins
import random
import string


def seed_generator(secret, seed_start=0, seed_stop=1):
    """Generates iota seeds from a given secret to a desired depth

    Type:
        Generator

    Args:
        secret  (str object, required) string object
        seed_start  (int object, required) integer defining subseed starting point
        seed_stop  (int object, required) integer defining subseed ending point

    Yields:
        string object (str): 90 character iota seed
    """

    # Tests
    if seed_start < 0 or seed_stop < 0:
        raise ValueError('Seed index cannot be negative')

    # Set alphas and initialise pseudo random number generator
    alphas = (string.ascii_uppercase + '9')
    random.seed(secret, version=2)

    for depth in range(seed_start, seed_stop):
        seed = "".join([alphas[random.randrange(27)] for i in range(81)])

        yield seed
