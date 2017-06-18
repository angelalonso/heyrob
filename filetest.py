import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import PatternMatchingEventHandler

class MyHandler(PatternMatchingEventHandler):

    def process(self, event):
        print("I am being processed")

    def on_modified(self, event):
        print("file modified " + event.src_path)
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

def test_out():
    print("Hell, yeah")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = "/home/pi/voice_in_web/recordings"
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
