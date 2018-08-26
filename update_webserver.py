import sys
import time
import os
import getopt
from shutil import copyfile
from shutil import move
from time import sleep

def add_file(infile):
    latestfolder = "/home/pi/webcam_latest/"
    head, tail = os.path.split(infile)
    fnameonly = tail
    newfile = latestfolder + fnameonly[:fnameonly.find("_")]
    copyfile(infile, newfile)  # Copy the modified new file from the MyCloud server back for the web server
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
    else:
        print ("File does not exist : " + newfile)

def usage():
    print('usage : update_webserver.py -i <file>')

def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:", ["ifile="])
    except getopt.GetoptError as err:
        print str(err)
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
    add_file(inputfile)

if __name__ == "__main__":
   main(sys.argv[1:])