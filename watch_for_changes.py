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
from subprocess import call


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
        outdirectory = "/mnt/mycloud/wernerterreblanche/webcam_backup/"


        print(event.src_path, event.event_type)  # print now only for debug
        if event.is_directory == False and event.event_type == 'created':
            filename = os.path.basename(event.src_path)
            infilepath = os.path.abspath(event.src_path)
            infile = event.src_path
            outfile = outdirectory + filename

            # create text that will be added to the picture
            textstr = "python " + basepath + "get_datetime.py -i " + infilepath
            p = Popen(shlex.split(textstr), stdin=PIPE, stdout=PIPE)
            datetime = (p.stdout.readline()).decode('utf-8')  # read the first line
            newtxt = datetime.replace('\n', '').replace('\r', '')  # remove newline

            # add the text to the picture and save it in its new location
            outputpath = os.path.join(outdirectory, newtxt + ".jpg")
            convertstr = "python " + basepath + "add_text.py -i " + infilepath + " -o " + outputpath + " -t " + newtxt
            call(shlex.split(convertstr))

            # Update the web server with the latest files
            convertstr = "python " + basepath + "update_webserver.py -i " + outputpath
            call(shlex.split(convertstr))


            # Remove the file from the SD CARD
            removestr = "rm " + infilepath
            print(removestr);
            runpython(removestr)


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

