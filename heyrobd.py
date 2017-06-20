#!/usr/bin/env python

import sys
import time
import logging
import subprocess
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import PatternMatchingEventHandler

class MyHandler(PatternMatchingEventHandler):

    def process(self, event):
        process_voice()

    def on_modified(self, event):
        print("new command detected at " + event.src_path)
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

def process_voice():
    cmd = './stt.sh'
    child = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)
    while True:
        out = child.stderr.read(1)
        if out == '' and child.poll() != None:
            break
        if out != '':
            sys.stdout.write(out)
            sys.stdout.flush()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = "./web/recordings"
    #event_handler = LoggingEventHandler()
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
