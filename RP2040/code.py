# Placeholder code for testing

# Standard Library
import time

# CircuitPython Core Modules
import board
import digitalio
import rp2pio
import supervisor

# Adafruit CircuitPython Library
import adafruit_pioasm

# Dim neopixel
supervisor.set_rgb_status_brightness(6)

# Simple PIO to read from a pin
hello = """
in pins, 32
"""

# LED for testing
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    print(1)
    time.sleep(0.001)

hello_program = """
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
"""