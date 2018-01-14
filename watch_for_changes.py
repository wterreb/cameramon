import sys
import time
import os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from shutil import copyfile
from shutil import move
from subprocess import Popen, PIPE
from time import sleep
import shlex

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
        print(event.src_path, event.event_type)  # print now only for debug
        if event.is_directory == False and event.event_type == 'created':
            filename = os.path.basename(event.src_path)
            filefullpath = os.path.abspath(event.src_path)

            # Get the datetime string
            datestr = "python /home/pi/scripts/python/get_datetime.py -i " + filename
            p = Popen(shlex.split(datestr), stdin=PIPE, stdout=PIPE)
            datetimestr =  p.stdout.readline().decode('utf-8') # read the first line
            datetimestr = datetimestr.replace('\n', ' ').replace('\r', '')  # remove newline

            #filepath = os.path.dirname(os.path.abspath(event.src_path))
            backup_filepath = "/mnt/mycloud/wernerterreblanche/webcam_backup/"
            #newfile = filepath + "webcam_latest/" + filename[:filename.find("_")]
            newfile = "/home/pi/webcam_latest/" + filename[:filename.find("_")]

	        # Add datetime info to the image
            addtextcmd = "python /home/pi/scripts/python/add_text.py -i " + event.src_path + " -o " + newfile + " -t '" + datetimestr + "'"
            print(addtextcmd)
            p = Popen(shlex.split(addtextcmd), stdin=PIPE, stdout=PIPE, stderr=PIPE)
            print (p.stdout.readline())
            sleep(2)  # Wait up to 2 seconds for the file to be created

            # Create all latest files if they do no yet exist (This should only happen once)
            if os.path.isfile(newfile + "_10.jpg") == False :
                copyfile(newfile, newfile + "_0.jpg")
                copyfile(newfile, newfile + "_1.jpg")
                copyfile(newfile, newfile + "_2.jpg")
                copyfile(newfile, newfile + "_3.jpg")
                copyfile(newfile, newfile + "_4.jpg")
                copyfile(newfile, newfile + "_5.jpg")
                copyfile(newfile, newfile + "_6.jpg")
                copyfile(newfile, newfile + "_7.jpg")
                copyfile(newfile, newfile + "_8.jpg")
                copyfile(newfile, newfile + "_9.jpg")
                copyfile(newfile, newfile + "_10.jpg")

            if os.path.isfile(newfile):
                sleep(0.1)
                move(newfile + "_9.jpg", newfile + "_10.jpg")
                sleep(0.1)
                move(newfile + "_8.jpg", newfile + "_9.jpg")
                sleep(0.1)
                move(newfile + "_7.jpg", newfile + "_8.jpg")
                sleep(0.1)
                move(newfile + "_6.jpg", newfile + "_7.jpg")
                sleep(0.1)
                move(newfile + "_5.jpg", newfile + "_6.jpg")
                sleep(0.1)
                move(newfile + "_4.jpg", newfile + "_5.jpg")
                sleep(0.1)
                move(newfile + "_3.jpg", newfile + "_4.jpg")
                sleep(0.1)
                move(newfile + "_2.jpg", newfile + "_3.jpg")
                sleep(0.1)
                move(newfile + "_1.jpg", newfile + "_2.jpg")
                sleep(0.1)
                move(newfile + "_0.jpg", newfile + "_1.jpg")
                sleep(0.1)
                copyfile(newfile, newfile + "_0.jpg")
                sleep(0.1)
                copyfile(newfile, backup_filepath  + filename)  # Copy the modified new file to the MyCloud server
            else:
                print ("File does not exist : " + newfile)

            os.remove(newfile)
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

