#!/usr/bin/env python3
''' heyrobd.py
Main program that controls the robot
'''

import os
import time
import logging
import subprocess
import inspect

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

import understand

PATH = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))


class WatchdogMyHandler(PatternMatchingEventHandler):

    def process(self, event):
        process_voice()

    def on_modified(self, event):
        print("...")
        self.process(event)

    def on_created(self, event):
        print("file created" + event.src_path)
        self.process(event)

    def on_moved(self, event):
        print("file moved" + event.src_path)
        self.process(event)

    def on_deleted(self, event):
        print("file deleted" + event.src_path)
        self.process(event)


class FilePolling(object):
    '''
    https://stackoverflow.com/questions/182197/how-do-i-watch-a-file-for-changes

    '''
    def __init__(self, pathtofile):
        self._cached_stamp = 0
        self.filename = pathtofile
        print (self.filename)

    def watch(self):
        stamp = os.stat(self.filename).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp
            process_voice()


def process_voice():
    # PATH at the end is needed for the script to know the main path
    cmd = PATH + '/stt.sh ' + PATH
    child = subprocess.Popen(cmd, shell=True, stderr=open('/dev/null', 'w'),
                             stdout=subprocess.PIPE, universal_newlines=True)
    out = child.communicate()
    print(str(understand.go(out, PATH)))

# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO,
#                         format='%(asctime)s - %(message)s',
#                         datefmt='%Y-%m-%d %H:%M:%S')
#     path = PATH + "/web/recordings/voice.wav"
#     pub = FilePolling(path)
#     while True:
#         try:
#             time.sleep(1)
#             pub.watch()
#         except KeyboardInterrupt:
#             print('\nDone')
#             break


if __name__ == "__main__":
    print(PATH)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = PATH + "/web/recordings"
    # event_handler = LoggingEventHandler()
    event_handler = WatchdogMyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    try:
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
    except OSError:
        print(path + " does not exist, or is not accessible")
