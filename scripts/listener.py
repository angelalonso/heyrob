#!/usr/bin/env python

import alsaaudio
import audioop
import time

from subprocess import call

THRESHOLD = 600
CHECKTIME = .01


def confirmation():
    call(["play", "../audio/listening.wav"])

input = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK)

input.setchannels(1)
input.setrate(8000)
input.setformat(alsaaudio.PCM_FORMAT_S16_LE)

input.setperiodsize(160)

while True:
    # Read data from device
    l, data = input.read()
    if l:
        # maximum of the absolute value of all samples in a fragment.
        sound = audioop.max(data, 2)
        if sound > THRESHOLD:
            print "Sound is going on"
            confirmation()
        else:
            print "-"

    time.sleep(CHECKTIME)
