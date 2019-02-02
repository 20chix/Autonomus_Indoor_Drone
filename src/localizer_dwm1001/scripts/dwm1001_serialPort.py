#!/usr/bin/env python

__author__     = "Hadi Elmekawi"
__version__    = "1.0"
__maintainer__ = "Hadi Elmekawi"
__email__      = "w1530819@my.westminster.ac.uk"
__status__     = "Development"


import serial

class SERIAL_PORT_DETAILS:
        name     = '/dev/ttyACM0'
        baudRate = 115200 
        parity   = serial.PARITY_ODD
        stopbits = serial.STOPBITS_TWO
        bytesize = serial.SEVENBITS
