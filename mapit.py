#! python3

import sys
import webbrowser
import logging

logging.basicConfig(filename='mapit.log', level=logging.DEBUG)

if len(sys.argv) <= 1:
    webbrowser.open('http://maps.google.com')
else:
    address = '+'.join(sys.argv[1:])
    logging.info(address)
    webbrowser.open('http://www.google.com/maps/search/{}'.format(address))
