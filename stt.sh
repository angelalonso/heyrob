#!/bin/bash
#TODO: if THISPATH is empty: pwd
#TODO: output mock result if no internet
#TODO: improve exit status for the script calling this know handle errors

THISPATH=$1

KEY=$(cat $THISPATH/scripts/.credentials)
SNDFILE="$THISPATH/test.wav"
SND2="$THISPATH/test.flac"



cp $THISPATH/web/recordings/voice.wav $SNDFILE
rm output.pcm 2>/dev/null
rm $SND2 2>/dev/null
ffmpeg -i $SNDFILE -ar 16k $SND2 -loglevel quiet

curl -X POST --data-binary @$SND2 --user-agent 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7' --header 'Content-Type: audio/x-flac; rate=16000;' 'https://www.google.com/speech-api/v2/recognize?output=json&lang=en-us&key='$KEY
