#!/usr/bin/env bash

# ADD YOUR CREDENTIALS TO THE FILE FIRST!
KEY=$(cat .credentials)
# EDIT THIS
AUDIO="../audio/you_are_listening_001.flac"

curl -X POST \
--data-binary @${AUDIO} \
--user-agent 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7' \
--header 'Content-Type: audio/x-flac; rate=16000;' \
'https://www.google.com/speech-api/v2/recognize?output=json&lang=en-us&key='${KEY}''
