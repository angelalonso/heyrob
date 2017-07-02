#!/usr/bin/env bash

VLC=$(which vlc)
YTB_URL="https://www.youtube.com/watch?v=MIJ4q9jmnIY"
$VLC -I dummy "${YTB_URL}" --vout none 2>/dev/null
