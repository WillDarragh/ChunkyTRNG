# Chunky TRNG (True Random Number Generator)

# Python Standard library
import random

# 3rd party libraries
from plotille import histogram


class ChunkyTRNG(random.Random):
    def __init__(self):
        super().__init__(self)


# If run as main, perform a test
if __name__ == '__main__':

    rng = ChunkyTRNG()

    results = [rng.random() for i in range(1_000_000)]

    print(histogram(results))
