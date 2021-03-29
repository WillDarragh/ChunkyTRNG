# Placeholder code for testing

import time
import board
import rp2pio
import adafruit_pioasm

hello = """
.program hello
in pins, 32
"""

assembled = adafruit_pioasm.assemble(hello)

sm = rp2pio.StateMachine(
    assembled,
    frequency=125000000,
    first_in_pin=board.D5,
    auto_push=True
)
print('real frequency:', sm.frequency)

reading = bytearray(1)

for i in range(100000):
    sm.readinto(reading)

print('done')