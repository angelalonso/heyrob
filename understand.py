#!/usr/bin/env python
''' This script receives the result of an STT tool and decides what to do next
'''
from subprocess import call

import takeaction

import subprocess
import time
import audioop
import alsaaudio
import json
import urllib2


def prepare_input(in_tuple):
    json_txt_escapes = str(in_tuple).split('\\n')[1]
    json_txt = json_txt_escapes.replace('\\', '')
    decoder = json.JSONDecoder()
    json_txt_len = len(json_txt)

    objs = []
    end = 0
    while end != json_txt_len:
        try:
            obj, end = decoder.raw_decode(json_txt, idx=end)
            objs.append(obj)
        except ValueError:
            print("ERROR")
            print(json_txt)


    found_list = []
    try:
        for item in objs[0]['result'][0]['alternative']:
            found_list.append(item['transcript'])
        return found_list
    except IndexError:
        return "Index NO RESULTS -> " + str(objs)
    except KeyError:
        return "Key NO RESULTS -> " + str(objs)


def go(in_tuple):
    understood = str(prepare_input(in_tuple))
    takeaction.action_write(understood)

    return understood
