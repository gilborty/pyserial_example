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

default_port = '/dev/ttyUSB0'
default_baud_rate = 115200

def get_serial_ports():
    """ Lists available serial ports
        
        :returns:
            A list of serial ports available
    """ 
    ports = glob.glob('/dev/tty[A-Za-z]*')
    
    available_ports = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            available_ports.append(port)
        except(OSError, serial.SerialException):
            pass
    return available_ports


