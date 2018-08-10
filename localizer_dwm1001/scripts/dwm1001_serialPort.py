#!/usr/bin/env python
import serial

class SERIAL_PORT_DETAILS:
        name     = '/dev/ttyACM0'
        baudRate = 115200 
        parity   = serial.PARITY_ODD
        stopbits = serial.STOPBITS_TWO
        bytesize = serial.SEVENBITS
