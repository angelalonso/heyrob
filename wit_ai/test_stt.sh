#!/usr/bin/env bash

TOKEN=$(cat .credentials)
curl -XPOST 'https://api.wit.ai/speech?v=20160526' \
   -i -L \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: audio/wav" \
   --data-binary "@sample.wav"
