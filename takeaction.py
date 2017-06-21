#!/usr/bin/env python
''' This script executes actions, calling scripts and stuff
'''
import time
import datetime

PATH = "/home/pi/heyrob"

def action_write(text_in):
    outputfile = open(PATH + "/testfile.txt", "a")
    outputfile.write(str(datetime.datetime.now()) + " - " + text_in + "\n")
    outputfile.close()


