#!/usr/bin/env python3
'''  takeaction.py
This script executes actions, calling scripts and stuff
'''

import datetime
import logging


def action_write(text_in, PATH):
    '''
    Write tet to a file
    '''
    log = setup_logging()

    log.debug('opening file')
    outputfile = open(PATH + "/result.txt", "a")

    log.debug('writing the following: ' + str(datetime.datetime.now())
              + " - " + text_in)
    outputfile.write(str(datetime.datetime.now()) + " - " + text_in + "\n")

    log.debug('closing file')
    outputfile.close()


def setup_logging():
    # TODO: Use an initlogger when all my files have logging enabled
    #  https://stackoverflow.com/questions/4375669/logging-in-python-with-config-file-using-handlers-defined-in-file-through-code#4376218
    '''
    Setup the Logging for this library only
    '''
    logger = logging.getLogger('takeaction_logger')
    logger.setLevel(logging.ERROR)
    fh = logging.FileHandler('log.takeaction.log')
    fh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s \
        - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
    logger.addHandler(fh)
    return logger
