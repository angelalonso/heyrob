#!/usr/bin/env bash
# Script to encode audio and send it to GSpeech

# The path might be passed as a parameter
THISPATH=$1
if [[ ! -z $"{THISPATH}" ]]; then
  THISPATH=$(pwd)
fi

# These are used to catch errors and give a mocked-up answer
ERROUT="$THISPATH/stderr.txt"
OKOUT="$THISPATH/stdout.txt"
MOCKOUT="$THISPATH/stt_mockup_result.txt"

# More vars
KEY=$(cat $THISPATH/scripts/.credentials)
SNDFILE="$THISPATH/test.wav"
SND2="$THISPATH/test.flac"

# Modify the original audio file to google's likings
cp $THISPATH/web/recordings/voice.wav $SNDFILE
rm output.pcm 2>/dev/null
rm $SND2 2>/dev/null
ffmpeg -i $SNDFILE -ar 16k $SND2 -loglevel quiet

# Call google pseech API
curl -X POST --data-binary @$SND2 --user-agent 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7' --header 'Content-Type: audio/x-flac; rate=16000;' 'https://www.google.com/speech-api/v2/recognize?output=json&lang=en-us&key='$KEY > $OKOUT 2> $ERROUT

# Now if anything went wrong, we send a mocked-up answer with a "not OK" exit code instead of just failing
if [[ $? -gt 0 ]]; then
  cat $MOCKOUT
  EXITCODE=3
else
  cat $OKOUT
  EXITCODE=0
fi

# CLean up, exit
rm $ERROUT
rm $OKOUT
exit $EXITCODE
