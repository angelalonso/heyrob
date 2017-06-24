# heyrobd.py

USE ALWAYS PYTHON3!

apt install python3-pip libasound2-dev
pip3 install watchdog pyalsaaudio

Tried but did not work:
```also add into /etc/rc.local :
mv /home/pi/heyrob/heyrobd.log.0 /home/pi/heyrob/heyrobd.log.1 2>/dev/null
mv /home/pi/heyrob/heyrobd.log /home/pi/heyrob/heyrobd.log.0 2>/dev/null
/usr/bin/python /home/pi/heyrob/heyrobd.py > /home/pi/heyrob/heyrobd.log
```


# voice_in_web

apt install php (comes with apache in debian unless php5-cgi is installed ->https://justinnewman.com/HOWTO/php-without-Apache)
apache or nginx + config file (only need to change the root folder)

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

# ERRORS
'''ERROR
<html lang=en>'''
- Happens when running from a cronjob
- Also when nothing is being recorded
- Also on fresh install running python3
- Problem seems with watchdog (alternative?)

