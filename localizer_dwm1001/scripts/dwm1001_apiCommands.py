#!/usr/bin/env python

class DWM1001_API_COMMANDS:
        DoubleEnter     = b'\r\r'  #ASCII char for double Enter
        SingleEnter     = b'\r'    #ASCII char for single Enter
        Lec             = b'lec'   #Show meas. and pos. in CSV      
        LecPlusEnter    = b'lec\r' #Show meas. and pos. in CSV then Enter
        Quit            = 'quit\r'#Quit API shell mode
        
        