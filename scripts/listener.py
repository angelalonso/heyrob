#!/usr/bin/env python

import alsaaudio
import audioop
import pyglet
import time

THRESHOLD = 600
CHECKTIME = .01


def confirmation():
    # http://stackoverflow.com/questions/307305/play-a-sound-with-python
    # also sample from http://www.noiseaddicts.com/free-samples-mp3/?id=3739
    music = pyglet.resource.media('../audio/noiseaddicts.com_samples_1w72b820_3739.mp3')
    music.play()

    pyglet.app.run()


input = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK)

input.setchannels(1)
input.setrate(16000)
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
