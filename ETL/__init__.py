import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def add_to_log(event):
    LOG_PATH = os.path.join(ROOT_DIR, 'ETL/log.txt')
    with open(LOG_PATH, 'w') as f:
        f.write(f"{event}\n")
