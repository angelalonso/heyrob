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

## On regularx4 laptop with Debian testing
sudo apt-get install yasm nasm \
                build-essential automake autoconf \
                libtool pkg-config libcurl4-openssl-dev \
                intltool libxml2-dev libgtk2.0-dev \
                libnotify-dev libglib2.0-dev libevent-dev \
                checkinstall
git clone git://git.videolan.org/ffmpeg.git
cd ffmpeg
./configure --prefix=/usr
time make -j 8
cat RELEASE
sudo mkdir -p /usr/share/ffmpeg
sudo checkinstall

# Bluetooth speaker
apt install pulseaudio-module-bluetooth expect

# ERRORS
'''ERROR
<html lang=en>'''
- Happens when running from a cronjob
- Also when nothing is being recorded
- Also on fresh install running python3
- Hint: Problem seems with watchdog
  - Not the case, polling gives same error
- Hint: 2017-06-25 07:10:02 - received - ('<!DOCTYPE html>\n<html lang=en>\n  <meta charset=utf-8>\n  <meta name=viewport content="initial-scale=1, minimum-scale=1, width=device-width">\n  <title>Error 403 (Forbidden)!!1</title>\n  <style>\n    *{margin:0;padding:0}html,code{font:15px/22px arial,sans-serif}html{background:#fff;color:#222;padding:15px}body{margin:7% auto 0;max-width:390px;min-height:180px;padding:30px 0 15px}* > body{background:url(//www.google.com/images/errors/robot.png) 100% 5px no-repeat;padding-right:205px}p{margin:11px 0 22px;overflow:hidden}ins{color:#777;text-decoration:none}a img{border:0}@media screen and (max-width:772px){body{background:none;margin-top:0;max-width:none;padding-right:0}}#logo{background:url(//www.google.com/images/branding/googlelogo/1x/googlelogo_color_150x54dp.png) no-repeat;margin-left:-5px}@media only screen and (min-resolution:192dpi){#logo{background:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) no-repeat 0% 0%/100% 100%;-moz-border-image:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) 0}}@media only screen and (-webkit-min-device-pixel-ratio:2){#logo{background:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) no-repeat;-webkit-background-size:100% 100%}}#logo{display:inline-block;height:54px;width:150px}\n  </style>\n  <a href=//www.google.com/><span id=logo aria-label=Google></span></a>\n  <p><b>403.</b> <ins>That\xe2\x80\x99s an error.</ins>\n  <p>Your client does not have permission to get URL <code>/speech-api/v2/recognize?output=json&amp;lang=en-us&amp;key=</code> from this server. Invalid key. <ins>That\xe2\x80\x99s all we know.</ins>\n', None)

