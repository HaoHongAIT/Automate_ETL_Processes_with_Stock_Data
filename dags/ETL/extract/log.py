from dags.ETL import *


def add_to_log(event):
    with open(LOG_PATH, 'a') as f:
        f.write(f"{event}\n")


