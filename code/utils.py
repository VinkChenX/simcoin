import time
import logging
import config
import sys
import os
import re
import json
from collections import namedtuple
import csv
import fcntl


def sleep(seconds):
    logging.debug("Sleep for {} seconds".format(seconds))
    time.sleep(seconds)


def check_equal(lst):
    return not lst or lst.count(lst[0]) == len(lst)


def config_logger(verbose):
    log_formatter = logging.Formatter("%(asctime)s.%(msecs)03d000 [%(processName)s-%(threadName)-12.12s] "
                                      "[%(levelname)-5.5s]  %(message)s", "%Y-%m-%d %H:%M:%S")
    logging.Formatter.converter = time.gmtime
    root_logger = logging.getLogger()

    file_handler = logging.FileHandler(config.log_file, mode='w')
    file_handler.setFormatter(log_formatter)
    root_logger.addHandler(file_handler)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_formatter)
    root_logger.addHandler(console_handler)

    if verbose:
        root_logger.setLevel(logging.DEBUG)
    else:
        root_logger.setLevel(logging.INFO)


def check_for_file(file):
    if not os.path.isfile(file):
        command = re.split('\.|/', file)[-2]
        print("{} file not found. Please generate this with the command `python3 simcoin.py {} [args]."
              .format(file, command))
        exit(-1)


def update_args_json(args):
    raw_data = {}
    if os.path.isfile(config.args_json):
        with open(config.args_json, 'r') as file:
            raw_data = json.load(file)

    raw_data.update(vars(args))
    data = {k: v for k, v in raw_data.items() if v is not None}

    with open(config.args_json, 'w') as file:
        file.write('{}\n'.format(json.dumps(data)))


def read_json_file(file):
    with open(file) as file:
        return json.loads(file.read(), object_hook=json_object_hook)


def json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())


def write_csv(file_name, elements, tag):
    with open(file_name, 'a') as file:
        logging.debug('Waiting for lock to write to file={}'.format(file_name))
        fcntl.flock(file, fcntl.LOCK_EX)
        logging.debug('Received lock for writing to file={}'.format(file_name))

        w = csv.writer(file, delimiter=';')
        for i, element in enumerate(elements):
            row = element.vars_to_array()
            if i != 0:
                row.append(tag)
            w.writerow(row)
