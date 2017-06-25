#!/usr/bin/env python3
''' understand.py
This script receives the result of an STT tool and decides what to do next
'''

import takeaction
import json
import logging


def prepare_input(in_tuple):
    '''
    Prepare the text received into something usable by JSON,
      then save it into a list
    '''
    log = setup_logging()

    log.debug('received - ' + str(in_tuple))
    json_txt_escapes = str(in_tuple).split('\\n')[1]
    log.debug('json_txt_escapes - ' + str(json_txt_escapes))
    json_txt = json_txt_escapes.replace('\\', '')
    log.debug('json_txt - ' + str(json_txt))
    decoder = json.JSONDecoder()
    json_txt_len = len(json_txt)

    objs = []
    end = 0
    while end != json_txt_len:
        try:
            obj, end = decoder.raw_decode(json_txt, idx=end)
            objs.append(obj)
        except ValueError:
            print("Value Error decoding Json text")
            print(json_txt)
            end = json_txt_len

    found_list = []
    try:
        for item in objs[0]['result'][0]['alternative']:
            found_list.append(item['transcript'])
        return found_list
    except IndexError:
        return "Index NO RESULTS -> " + str(objs)
    except KeyError:
        return "Key NO RESULTS -> " + str(objs)


def go(in_tuple, PATH):
    '''
    Control the understanding process
    '''
    log = setup_logging()

    understood = str(prepare_input(in_tuple))
    log.debug('understood - ' + understood)
    # Here, PATH is needed to run actions from a cronjob as well
    takeaction.action_write(understood, PATH)

    return understood


def setup_logging():
    # TODO: Use an initlogger when all my files have logging enabled
    #  https://stackoverflow.com/questions/4375669/logging-in-python-with-config-file-using-handlers-defined-in-file-through-code#4376218
    '''
    Setup the Logging for this library only
    '''
    logger = logging.getLogger('understand_logger')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('log.understand.log')
    fh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s \
        - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
    logger.addHandler(fh)
    return logger
