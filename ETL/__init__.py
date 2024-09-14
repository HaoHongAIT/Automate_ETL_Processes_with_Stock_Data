import os
import sys
from datetime import date

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
TODAY = date.today().strftime(r"%d/%m/%Y")
LOG_PATH = os.path.join(PACKAGE_DIR, 'log.txt')

if not os.path.exists(TODAY):
    with open(LOG_PATH, 'w') as file:
        pass

