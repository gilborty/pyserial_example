#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    Super simple example of using the PySerial module to blink and LED on an Arduino Uno
"""
import serial
import argparse
import glob
import sys 

#My own library for pretty print debug statements
import debug_status

def get_serial_ports():
    """ Lists available serial ports
        
        :returns:
            A list of serial ports available
    """ 
    ports = 


port = "/dev/ttyUSB0"
baud_rate = 115200


