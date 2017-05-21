#!/usr/bin/env python
''' This script listens for a higher volume recorded,
then waits for a keyword
then passes that to google speech
if ok, listens for the action
then passes that, too, to google speech
and finally triggers actions
'''
from subprocess import call

import subprocess
import time
import audioop
import alsaaudio
import json

import urllib2

THRESHOLD = 900
CHECKTIME = .001
AUDIORATE = 16000
CHANNELS = 1

# TODO: Probably set these as variables we pass on
KEYWORDFILE = "tmpkeyword.wav"
FLACFILE = "tmp.flac"


def noise_listen():
    '''Constantly listens for higher volumes on the input'''
    standby_input = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,
                                  alsaaudio.PCM_NONBLOCK)
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
    # TODO: record with alsaaudio instead of an external call
    cmd = "arecord -D plughw:1,0 -d 2 -r " + str(AUDIORATE) + " " + KEYWORDFILE
    subprocess.Popen([cmd], shell=True).communicate()
    return True


def confirmation():
    '''Plays confirmation that a sound has been identified'''
    call(["play", "../audio/beep.wav"])


def load_key():
    '''Loads the Google API key from the .credentials file
    PLEASE, MAKE SURE YOU HAVE IT READY!'''
    keyfile = ".credentials"
    key = ""
    with open(keyfile, 'r') as filebuffer:
        key = filebuffer.readline().strip()
    return key


def speechtotext():
    '''Transforms the recorded WAV into FLAC, then sends it to Google Speech
       , and returns the raw JSON-formatted result'''
    gapikey = load_key()
    cmd_transform = "flac " + KEYWORDFILE + " -f --best --sample-rate 16000 \
                     -o " + FLACFILE

    subprocess.Popen([cmd_transform], shell=True).communicate()

    url = 'https://www.google.com/speech-api/v2/recognize?output=json&lang=en-us&key=' \
    + gapikey 
    audio = open(FLACFILE,'rb').read()
    headers = {'Content-Type': 'audio/x-flac; rate=16000', 'User-Agent':'Mozilla/5.0'}
    request = urllib2.Request(url, data=audio, headers=headers)
    ret = urllib2.urlopen(request)
    responses = []
    responses = ret.read()
    curl_result_raw = json.loads(json.dumps(responses))
    
    print curl_result_raw
    



while True:
    # TODO: streamline the recognition process
    #       (first keyword, confirm, then action, confirm...)
    #       PROBABLY we need no signal that it is listening for the keyword,
    #       just after it has been recognized

    # TODO: Debug mode
    noise_in = noise_listen()
    if noise_in:
        keyword_in = keyword_listen()
        if keyword_in:
            confirmation()
            speechtotext()
