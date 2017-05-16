#!/usr/bin/env python

import alsaaudio
import audioop
import pyglet
import time


from wave import open as waveOpen
from ossaudiodev import open as ossOpen

THRESHOLD = 600
CHECKTIME = .01


def confirmation():
    # also sample from http://www.noiseaddicts.com/free-samples-mp3/?id=3739
    s = waveOpen('listening.wav','rb')
    (nc,sw,fr,nf,comptype, compname) = s.getparams( )
    dsp = ossOpen('/dev/dsp','w')
    try:
      from ossaudiodev import AFMT_S16_NE
    except ImportError:
      from sys import byteorder
      if byteorder == "little":
        AFMT_S16_NE = ossaudiodev.AFMT_S16_LE
      else:
        AFMT_S16_NE = ossaudiodev.AFMT_S16_BE
    dsp.setparameters(AFMT_S16_NE, nc, fr)
    data = s.readframes(nf)
    s.close()
    dsp.write(data)
    dsp.close()


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
