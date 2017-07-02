#!/bin/bash

HW="plughw:1,0"
DUR="3"

KEY=$(cat .credentials)
#SNDFILE="test.flac"
SNDFILE="test.wav"
SND2="test.flac"

#arecord -D $HW -t wav -d $DUR -r 16000 | flac - -f --best --sample-rate 16000 -o $SNDFILE


#curl -X POST --data-binary @$SNDFILE --user-agent 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7' --header 'Content-Type: audio/x-flac; rate=16000;' 'https://www.google.com/speech-api/v2/recognize?output=json&lang=en-us&key='$KEY
cp /home/aaf/Software/Dev/heyrob/web/recordings/voice.wav $SNDFILE
#cp /home/pi/voice_in_web/recordings/voice.wav $SNDFILE
rm output.pcm
rm $SND2
ffmpeg -i $SNDFILE -ar 16k $SND2
#ffmpeg -i aux.wav -f s16le -acodec pcm_s16le output.pcm
#ffmpeg -f s16le -ar 16k -ac 1 -i output.pcm $SNDFILE
#sox $SNDFILE $SND2

#curl -X POST --data-binary @$SNDFILE --user-agent 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7' --header 'Content-Type: audio/l16; rate=16000;' 'https://www.google.com/speech-api/v2/recognize?output=json&lang=en-us&key='$KEY
curl -X POST --data-binary @$SND2 --user-agent 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7' --header 'Content-Type: audio/x-flac; rate=16000;' 'https://www.google.com/speech-api/v2/recognize?output=json&lang=en-us&key='$KEY

#curl -X POST --data-binary @$SNDFILE --header "Content-Type: audio/l16; rate=16000;" "https://www.google.com/speech-api/v2/recognize?output=json&lang=en-us&key=$KEY"
