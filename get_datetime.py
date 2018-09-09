#!/usr/bin/python

import sys
import getopt
import os
import datetime

def extract(fname):
   #filename = "WashingRoom_2017060418493101.jpg"
   head, tail = os.path.split(fname)
   fnameonly = tail
   camera = fnameonly[:fnameonly.find("_")]
   filename = fname[fname.find("_")+1:]
   dtime = datetime.datetime.now()
   year = dtime.year
   month = dtime.month
   day = dtime.day
   hour = dtime.hour
   minute = dtime.minute
   second = dtime.second
   datestr = "%d_%02d_%02d_%02dh%02d_%02d" % (year, month, day, hour, minute, second)
   outstr = datestr + "_" + camera
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