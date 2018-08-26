#!/usr/bin/python

import sys
import getopt
import os

def extract(fname):
   #filename = "WashingRoom_2017060418493101.jpg"
   head, tail = os.path.split(fname)
   fnameonly = tail
   camera = fnameonly[:fnameonly.find("_")]
   filename = fname[fname.find("_")+1:]
   year = filename[:4]
   month = filename[4:6]
   day = filename[6:8]
   hour = filename[8:10]
   minute = filename[10:12]
   outstr = camera + " " + year + "/" + month + "/" + day + " " + hour + ":" + minute
   print(outstr)

def main(argv):
   inputfile = ''
   outputfile = ''
   text = ''
   try:
      opts, args = getopt.getopt(argv,"hi:",["ifile="])
   except getopt.GetoptError:
      print('get_datetime.py -i <inputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('usage : get_datetime.py -i <inputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
   extract(inputfile)

if __name__ == "__main__":
   main(sys.argv[1:])