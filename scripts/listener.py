#!/usr/bin/env python

from subprocess import call

import time
import audioop
import alsaaudio


THRESHOLD = 900
CHECKTIME = .01


def confirmation():
    call(["play", "../audio/listening.wav"])
    time.wait(3)

audio_input = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK)

audio_input.setchannels(1)
audio_input.setrate(8000)
audio_input.setformat(alsaaudio.PCM_FORMAT_S16_LE)

audio_input.setperiodsize(160)

while True:
    # Read data from device
    l, data = audio_input.read()
    if l:
        if l > 0:
            # maximum of the absolute value of all samples in a fragment.
            sound = audioop.max(data, 2)
            if sound > THRESHOLD:
                print "Sound is going on"
                confirmation()

    time.sleep(CHECKTIME)
