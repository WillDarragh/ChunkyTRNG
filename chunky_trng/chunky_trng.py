# Chunky TRNG (True Random Number Generator)

# Python Standard library
import random

# 3rd party libraries
from plotille import histogram
import serial

# TODO: automatically detect serial port
# https://github.com/mu-editor/mu/blob/f56bf64ff570d6268862b0396e79295031e6aedf/mu/modes/base.py


class ChunkyTRNG(random.Random):
    def __init__(self):
        super().__init__(self)


# If run as main, perform a test
if __name__ == '__main__':

    rng = ChunkyTRNG()

    results = [rng.random() for i in range(1_000_000)]

    print(histogram(results))
