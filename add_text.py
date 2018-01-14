#!/usr/bin/python

import sys
import getopt
import time
import os
import shlex
from subprocess import call

def convert(infile, outfile, text):
   convertcmd = "/usr/bin/convert " + infile + " -pointsize 30 -fill yellow -annotate +10+471 '" + text + "' " + outfile
   print(convertcmd)
   call(shlex.split(convertcmd))

def main(argv):
    inputfile = ""
    outputfile = ""
    text = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:t:",["ifile=","ofile=","text"])
    except getopt.GetoptError:
        print('add_text.py -i <inputfile> -o <outputfile> -t <displaytext>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('usage : add_text.py -i <inputfile> -o <outputfile> -t <displaytext>')
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




