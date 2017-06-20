#!/bin/bash

KEY=$(cat scripts/.credentials)
SNDFILE="test.wav"
SND2="test.flac"



cp ./web/recordings/voice.wav $SNDFILE
rm output.pcm 2>/dev/null
rm $SND2 2>/dev/null
ffmpeg -i $SNDFILE -ar 16k $SND2 -loglevel quiet

curl -X POST --data-binary @$SND2 --user-agent 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7' --header 'Content-Type: audio/x-flac; rate=16000;' 'https://www.google.com/speech-api/v2/recognize?output=json&lang=en-us&key='$KEY
