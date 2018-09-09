#!/usr/bin/python

import sys
import getopt
import time
import os
import shlex
from subprocess import call
from subprocess import Popen, PIPE
from time import sleep


def convert(infile, outfile, text):
   basepath = os.getcwd() + "/"
   convertcmd = "/usr/bin/convert " + infile + " -pointsize 30 -fill yellow -annotate +10+471 '" + text + "' " + \
                outfile
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
        opts, args = getopt.getopt(argv,"hi:o:t:",["help", "ifile=", "ofile-", "text=" ])
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
        elif opt in ("-t", "--text"):
            text = arg

    if os.name != 'nt':
        convert(inputfile, outputfile, text)
    else:
        print("Not converted on Windows PC")

if __name__ == "__main__":
   main(sys.argv[1:])




