import os

import sys
import getopt
from subprocess import Popen, PIPE
import shlex

def movefiles(indirectory, outdirectory):

    basepath = "/home/pi/projects/cameramon/"
    if os.name == 'nt':  # sys.platform == 'win32':
        basepath = "C:/Users/werne/projects/cameramon/"

    # Walk the tree.
    for root, directories, files in os.walk(indirectory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            infilepath = os.path.join(indirectory, filename)
            outputpath = os.path.join(outdirectory, filename)
            print("Reading : " + infilepath)
            print("Writing : " + outputpath)

            # Add text to picture and move it to the output folder
            textstr = "python " + basepath + "get_datetime.py -i " + filename
            p = Popen(shlex.split(textstr), stdin=PIPE, stdout=PIPE)
            datetime =  (p.stdout.readline()).decode('utf-8') # read the first line
            datetime = datetime.replace('\n', ' ').replace('\r', '')  # remove newline

            convertstr = "python " + basepath + "add_text.py -i " + infilepath + " -o " + outputpath + " -t '" + datetime + "'"
            p = Popen(shlex.split(convertstr), stdin=PIPE, stdout=PIPE)
            outstr =  (p.stdout.readline()).decode('utf-8') # read the first line
            outstr = outstr.replace('\n', ' ').replace('\r', '')  # remove newline
            print(outstr)

	    removestr = "rm " + infilepath
            print("Deleting : " + infilepath);
            p = Popen(shlex.split(removestr), stdin=PIPE, stdout=PIPE)
            outstr =  (p.stdout.readline()).decode('utf-8') # read the first line
            outstr = outstr.replace('\n', ' ').replace('\r', '')  # remove newline
            print(outstr)


def main(argv):
    infolder = "/home/pi/webcam/"
    outfolder = "/mnt/mycloud/wernerterreblanche/webcam_backup/"

    if os.name == 'nt':  # sys.platform == 'win32':
        infolder = "X:\\wernerterreblanche\\webcam"
        outfolder = "X:\\wernerterreblanche\\webcam_backup"
    movefiles(infolder,outfolder)

def main1(argv):
   inputfile = ''
   outputfile = ''
   text = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o",["idir=","odir="])
   except getopt.GetoptError:
      print('backup.py -i <in_directory> -o <out_directory>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('usage : python backup.py -i <in_directory> -o <out_directory>')
         sys.exit()
      elif opt in ("-i", "--idir"):
         inputdir = arg
      elif opt in ("-o", "--odir"):
         outputdir = arg

   movefiles(inputdir, outputdir)

if __name__ == "__main__":
   main(sys.argv[1:])
