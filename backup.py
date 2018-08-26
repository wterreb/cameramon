import os

import sys
import getopt
from subprocess import Popen, PIPE
import shlex


def runpython(strcmd):
    p = Popen(shlex.split(strcmd), stdin=PIPE, stdout=PIPE)
    outstr = (p.stdout.readline()).decode('utf-8')  # read the first line
    outstr = outstr.replace('\n', ' ').replace('\r', '')  # remove newline
    print(outstr)

def movefiles(indirectory, outdirectory):

    basepath = "/home/pi/projects/cameramon/"
    if os.name == 'nt':  # sys.platform == 'win32':
        basepath = "C:/Work/raspberry/projects/cameramon/"

    # Walk the tree.
    for root, directories, files in os.walk(indirectory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            infilepath = os.path.join(indirectory, filename)
            outputpath = os.path.join(outdirectory, filename)
            print("Reading : " + infilepath)
            print("Writing : " + outputpath)

            # Add text to picture and move it to the output folder
            convertstr = "python " + basepath + "add_text.py -i " + infilepath + " -o " + outputpath
            runpython(convertstr)

            # Update the web server with the latest files
            convertstr = "python " + basepath + "update_webserver.py -i " + outputpath
            runpython(convertstr)

            # Remove the file from the SD CARD
            removestr = "rm " + infilepath
            print("Deleting : " + infilepath);
            runpython(removestr)

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
