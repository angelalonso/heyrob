#!/bin/bash

HW="plughw:1,0"
DUR="3"

KEY=$(cat .credentials)
SNDFILE="test.flac"
#SNDFILE="test.wav"

#arecord -D $HW -t wav -d $DUR -r 16000 | flac - -f --best --sample-rate 16000 -o $SNDFILE


curl -X POST --data-binary @$SNDFILE --user-agent 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7' --header 'Content-Type: audio/x-flac; rate=16000;' 'https://www.google.com/speech-api/v2/recognize?output=json&lang=en-us&key='$KEY



#curl -X POST --data-binary @$SNDFILE --user-agent 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7' --header 'Content-Type: audio/l16; rate=16000;' 'https://www.google.com/speech-api/v2/recognize?output=json&lang=en-us&key='$KEY

#curl -X POST --data-binary @$SNDFILE --header "Content-Type: audio/l16; rate=16000;" "https://www.google.com/speech-api/v2/recognize?output=json&lang=en-us&key=$KEY"
