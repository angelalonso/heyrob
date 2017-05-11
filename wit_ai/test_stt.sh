#!/usr/bin/env bash

TOKEN=$(cat .credentials)

arecord -D plughw:1,0 -d 3 sample.wav

lame -h sample.wav sample.mp3

curl -XPOST 'https://api.wit.ai/speech?v=20170307' \
   -i -L \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: audio/mpeg3" \
   --data-binary "@sample.mp3"
