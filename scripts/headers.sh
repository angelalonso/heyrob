#!/bin/bash
    echo "$1"
    ffmpeg -y -i "$1" -f wav out.wav > /dev/null 2>&1 && \
    normalize-audio -q out.wav && \
    lame --silent -a -m m --cbr -b 64 -q 0 out.wav out.mp3 && \
    ffmpeg -y -i out.mp3 -f wav -acodec copy "$1" > /dev/null 2>&1 && \
    echo "done."
