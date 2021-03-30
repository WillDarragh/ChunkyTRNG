"""This modules contains ChunkyTRNG class to interact with
the ChunkyTRNG CIRCUITPYTHON device

CLASSES
-------
ChunkyTRNG(random.Random)
    This is the main important class

MAIN
----
If run as main, with say python -m chunky_trng
the program will run a brief test of randomness,
graphing random() results to the command line
"""

# Python Standard library
import random
from os import name as os_name

# 3rd party libraries
import serial
from plotille import histogram
from PyQt5.QtSerialPort import QSerialPortInfo


# TODO: automatically detect serial port
# https://github.com/mu-editor/mu/blob/f56bf64ff570d6268862b0396e79295031e6aedf/mu/modes/base.py


class ChunkyTRNG(random.Random):
    """The main chunky"""

    def __init__(self, valid_boards=None):
        """Initializes instance of ChunkyTRNG class

        :param valid_boards: Optional list of valid board info of format
                             (vendor_identifier, product_identifier, manufacturer, device_name)
        """
        super().__init__(self)

        # Tested with Adafruit Feather RP2040
        adafruit_feather_board = (0x239A, None, None, "Adafruit Feather")
        self.valid_boards = valid_boards if valid_boards else [adafruit_feather_board]

        available_ports = QSerialPortInfo.availablePorts()

        for port in available_ports:
            if self.is_valid_board(port):
                port_name = port.portName()
                break
        else:
            raise self.ChunkyTRNGException()

        # OS specific port
        if os_name == "posix":
            port_path = f'/dev/{port_name}'
        elif os_name == "nt":
            port_path = port_name
        else:
            raise NotImplementedError(f"OS {os_name} not supported. That's a big chunky.")

        self.ser = serial.Serial(port_path)

    def is_valid_board(self, port):
        """Checks if a board is compatible

        :param port: QSerialPortInfo port info object
        """
        vid = port.vendorIdentifier()
        pid = port.productIdentifier()
        manufacturer = port.manufacturer()

        for v, p, m, _ in self.valid_boards:
            if (
                v == vid
                and (p == pid or p is None)
                and (m == manufacturer or m is None)
            ):
                return True

    class ChunkyTRNGException(Exception):
        """That's a chunky!"""

        def __init__(self):
            super().__init__("That's a Chunky!")


# If run as main, perform a test
if __name__ == '__main__':
    rng = ChunkyTRNG()

    results = [rng.random() for i in range(1_000_000)]

    print(histogram(results))
