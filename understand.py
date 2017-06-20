#!/usr/bin/env python
''' This script receives the result of an STT tool and decides what to do next
'''
from subprocess import call

import subprocess
import time
import audioop
import alsaaudio
import json
import urllib2


def actions(in_tuple):
    json_txt_escapes = str(in_tuple).split('\\n')[1]
    json_txt = json_txt_escapes.replace('\\', '')
    decoder = json.JSONDecoder()
    json_txt_len = len(json_txt)

    objs = []
    end = 0
    while end != json_txt_len:
        obj, end = decoder.raw_decode(json_txt, idx=end)
        objs.append(obj)

    found_list = []
    try:
        for item in objs[0]['result'][0]['alternative']:
            found_list.append(item['transcript'])
        return found_list
    except IndexError:
        return "Index NO RESULTS -> " + str(objs)
    except KeyError:
        return "Key NO RESULTS -> " + str(objs)

def noactions(in_tuple):
    input_raw = str(in_tuple)
    json_txt = input_raw.split('\n')[0]
    decoder = json.JSONDecoder()
    json_txt_len = len(json_txt)

    objs = []
    end = 0
    while end != json_txt_len:
        obj, end = decoder.raw_decode(json_txt, idx=end)
        objs.append(obj)

    found_list = []
    try:
        for item in objs[0]['result'][0]['alternative']:
            found_list.append(item['transcript'])
        return found_list
    except IndexError:
        return "Index NO RESULTS -> " + str(objs)
    except KeyError:
        return "Key NO RESULTS -> " + str(objs)

