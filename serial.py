"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """Generates serial numbers starting at start"""
        self.start = start
        self.serial_number= self.start

    def __repr__(self):
        """Representation of SerialGenerator class"""
        return f'<SerialGenerator start={self.start} serial_number={self.serial_number}>'
    
    def generate(self):
        """return next serial_number """
        self.serial_number += 1

        return self.serial_number -1
        
    
    def reset(self):
        """Resets the serial_number generated to the start value"""
        self.serial_number= self.start





