#!/usr/bin/python

import sys
import getopt
import time
import os
import shlex
from subprocess import call
from subprocess import Popen, PIPE
from time import sleep


def convert(infile, outfile):
   basepath = os.getcwd() + "/"
   #print(basepath)
   textstr = "python " + basepath + "get_datetime.py -i " + basepath + infile
   p = Popen(shlex.split(textstr), stdin=PIPE, stdout=PIPE)
   datetime = (p.stdout.readline()).decode('utf-8')  # read the first line
   datetimestr = datetime.replace('\n', '').replace('\r', '')  # remove newline
   convertcmd = "/usr/bin/convert " + infile + " -pointsize 30 -fill yellow -annotate +10+471 '" + datetimestr + "' " + outfile
   print(convertcmd)
   call(shlex.split(convertcmd))
   sleep(2)  # Wait up to 2 seconds for the file to be created

def usage():
    print('usage : add_text.py -i <inputfile> -o <outputfile>')

def main(argv):
    inputfile = ""
    outputfile = ""
    text = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["help", "ifile=", "ofile="])
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
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    if os.name != 'nt':
        convert(inputfile, outputfile)
    else:
        print("Not converted on Windows PC")

if __name__ == "__main__":
   main(sys.argv[1:])




