#!/usr/bin/env python

from dwm1001_systemDefinitions           import SYS_DEFS

__author__     = SYS_DEFS.AUTHOR
__version__    = SYS_DEFS.VERSION
__maintainer__ = SYS_DEFS.MAINTAINER
__email__      = SYS_DEFS.EMAIL
__status__     = SYS_DEFS.STATUS


import serial

class SERIAL_PORT_DETAILS:
        name     = '/dev/ttyACM0'
        baudRate = 115200
        parity   = serial.PARITY_ODD
        stopbits = serial.STOPBITS_TWO
        bytesize = serial.SEVENBITS
