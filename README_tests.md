# heyrobd.py

apt install python3-pip
pip3 install watchdog

also add into /etc/rc.local :
mv /home/pi/heyrob/heyrobd.log.0 /home/pi/heyrob/heyrobd.log.1 2>/dev/null
mv /home/pi/heyrob/heyrobd.log /home/pi/heyrob/heyrobd.log.0 2>/dev/null
/usr/bin/python /home/pi/heyrob/heyrobd.py > /home/pi/heyrob/heyrobd.log

# voice_in_web

php
nginx + config file

# Python JS server
pip3 install websockets gevent

# playing with formats

 ATTENTION: takes ~1h
http://www.jeffreythompson.org/blog/2014/11/13/installing-ffmpeg-for-raspberry-pi/
cd /usr/src
git clone git://git.videolan.org/x264
cd x264
./configure --host=arm-unknown-linux-gnueabi --enable-static --disable-opencl
make
sudo make install

 ATTENTION: takes almost 5h!

cd /usr/src
git clone https://github.com/FFmpeg/FFmpeg.git
cd ffmpeg
sudo ./configure --arch=armel --target-os=linux --enable-gpl --enable-libx264 --enable-nonfree
make
sudo make install

# Bluetooth speaker
apt install pulseaudio-module-bluetooth expect
