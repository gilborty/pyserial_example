# pyserial_example
Simple PySerial example.

## Tested on Ubuntu 14.04 x86_64 with Python 2.7.6

## Required Python modules
* [pyserial](https://pypi.python.org/pypi/pyserial)
* [argparse](https://pypi.python.org/pypi/argparse)

# Running it
* `cd pyserial_example`
* `python main.py --port [PORTNAME] --baud [BAUDRATE]`
* Type away!

The way I tested this was to setup a simple hardware loopback on `/dev/ttyUSB0` that just echo'd what I typed in the program.  



