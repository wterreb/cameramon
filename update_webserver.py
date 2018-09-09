import sys
import time
import os
import getopt
from shutil import copyfile
from shutil import move
from time import sleep
import re
from subprocess import Popen, PIPE
import shlex
import os.path


def runpython(strcmd):
    p = Popen(shlex.split(strcmd), stdin=PIPE, stdout=PIPE)
    outstr = (p.stdout.readline()).decode('utf-8')  # read the first line
    outstr = outstr.replace('\n', ' ').replace('\r', '')  # remove newline
    print(outstr)

def arrangefiles(sourcefile, newname):

    matchObj = re.search('(.*)\.', newname)
    newname = matchObj.group(1)

    for x in range(29, -1, -1):
        oldfile = newname + "_" + str(x) + ".jpg"
        newfile = newname + "_" + str(x + 1) + ".jpg"
        if os.path.isfile(oldfile):
            copyfile(oldfile, newfile)
        else:
            print ("Creating : " + oldfile)
            copyfile(sourcefile, oldfile)
        if x == 0:
            copyfile(sourcefile, oldfile) # file zero is the latest photo
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