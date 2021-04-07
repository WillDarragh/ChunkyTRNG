# Placeholder code for testing

# Standard Library
import time

# CircuitPython Core Modules
import board
import digitalio
import displayio
import rp2pio
import supervisor

# Adafruit CircuitPython Library
import adafruit_displayio_ssd1306
import adafruit_pioasm
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label

# Dim neopixel
supervisor.set_rgb_status_brightness(0)

# Simple PIO to read from a pin
hello = """
in pins, 32
"""

# LED for testing
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Display Testing
displayio.release_displays()

i2c = board.I2C()

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.D4)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

scrolling_text = displayio.Group(max_size=1)

text = 'Энди Сэмберг участвует в викторине Дэна Веги Mega Money Quiz, но сталкивается с неприятными неприятностями каждый раз, когда выбирает Коренастый на доске.'
font = bitmap_font.load_font("/NotoSansDisplay-Regular-48.pcf")
x = 0
y = 30

text_area = label.Label(text=text, font=font, x=x, y=y)

scrolling_text.append(text_area)

display.show(scrolling_text)

time.sleep(2)

while True:
    scrolling_text[0].x -= 1
    time.sleep(0.0075)

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