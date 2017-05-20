#!/usr/bin/env python

from subprocess import call

import time
import audioop
import alsaaudio
import subprocess


THRESHOLD = 900
CHECKTIME = .01
AUDIORATE = 8000
CHANNELS = 1

KEYWORDFILE = "tmpkeyword.wav"


def wake_confirm():
    '''Plays confirmation that a sound has been identified'''
    call(["play", "../audio/listening.wav"])
    time.sleep(3)


def standby_listen():
    '''Constantly listens for higher volumes on the input'''
    standby_input = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK)
    standby_input.setchannels(CHANNELS)
    standby_input.setrate(AUDIORATE)
    standby_input.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    standby_input.setperiodsize(160)

    while True:
        # Read data from device
        l, data = standby_input.read()
        if l:
            if l > 0:
                # maximum of the absolute value of all samples in a fragment.
                signal = audioop.max(data, 2)
                if signal > THRESHOLD:
                    print "Sound is going on"
                    return True
        time.sleep(CHECKTIME)


def keyword_listen():
    '''Records the keyword, for further recognition'''
    cmd = "arecord -D plughw:1,0 -d 3 " + KEYWORDFILE
    subprocess.Popen([cmd], shell=True).communicate()
    return True


def confirmation():
    '''Plays confirmation that a sound has been identified'''
    call(["play", "../audio/listening.wav"])

def original():

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

while True:
    triggered = standby_listen()
    if triggered:
        confirmation()
        print "HEY"
        trig2 = keyword_listen()
        if trig2:
            confirmation()
            print "HEY 2"

