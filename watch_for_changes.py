import sys
import time
import os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from shutil import copyfile
from shutil import move
from subprocess import Popen, PIPE
import shlex
from time import sleep


def runpython(strcmd):
    p = Popen(shlex.split(strcmd), stdin=PIPE, stdout=PIPE)
    outstr = (p.stdout.readline()).decode('utf-8')  # read the first line
    outstr = outstr.replace('\n', ' ').replace('\r', '')  # remove newline
    print(outstr)

class MyHandler(PatternMatchingEventHandler):
    patterns=["*.jpg"]

    def process(self, event):
        """
        event.event_type
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """

        #watchfolder = "/home/pi/webcam/"
        basepath = "/home/pi/projects/cameramon/"
        outfolder = "/mnt/mycloud/wernerterreblanche/webcam_backup/"


        print(event.src_path, event.event_type)  # print now only for debug
        if event.is_directory == False and event.event_type == 'created':
            filename = os.path.basename(event.src_path)
            filefullpath = os.path.abspath(event.src_path)
            infile = event.src_path
            outfile = outfolder + filename

            # Add date/time text to picture and save it it to the output folder
            convertstr = "python " + basepath + "add_text.py -i " + infile + " -o " + outfile
            runpython(convertstr)

            # Update the web server with the latest files
            convertstr = "python " + basepath + "update_webserver.py -i " + outfile
            runpython(convertstr)

            print('filefullpath = ' + filefullpath)
            os.remove(filefullpath)   # Delete the original file from the SD card

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)


if __name__ == '__main__':
    args = sys.argv[1:]
    print ("Watching folder : " + args[0])
    observer = Observer()
    observer.schedule(MyHandler(), path=args[0] if args else '.')
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

