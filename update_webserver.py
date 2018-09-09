import sys
import time
import os
import getopt
from shutil import copyfile
from shutil import move
from time import sleep
import re
import os.path


def arrangefiles(sourcefile, newname):

    matchObj = re.search('(.*)\.', newname)
    newname = matchObj.group(1)

    for x in range(9):
        oldfile = newname + "_" + str(x) + ".jpg"
        newfile = newname + "_" + str(x + 1) + ".jpg"
        if os.path.isfile(oldfile):
            copyfile(sourcefile, newfile)
        else:
            print ("Creating : " + newfile)
            copyfile(sourcefile, oldfile)
            sleep(0.1)

def add_file(infile):
    latestfolder = "/home/pi/webcam_latest/"
    head, tail = os.path.split(infile)
    fnameonly = tail
    matchObj = re.search('.*_(.*)', infile)
    newfile = latestfolder + matchObj.group(1)
    arrangefiles(infile, newfile)

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