# filetest.py

apt install python3-pip
pip3 install watchdog

# voice_in_web

php
nginx + config file

# playing with formats


http://www.jeffreythompson.org/blog/2014/11/13/installing-ffmpeg-for-raspberry-pi/
cd /usr/src
git clone git://git.videolan.org/x264
cd x264
./configure --host=arm-unknown-linux-gnueabi --enable-static --disable-opencl
make
sudo make install

cd /usr/src
git clone https://github.com/FFmpeg/FFmpeg.git
cd ffmpeg
sudo ./configure --arch=armel --target-os=linux --enable-gpl --enable-libx264 --enable-nonfree
make
sudo make install
