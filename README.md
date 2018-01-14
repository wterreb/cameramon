WebCam cameras have to be set up to FTP to the Raspberry Pi as follows:
Dest folder : home/pi/webcam/
FTP user : pi
password :raspberry

The script watch_for_changes.py will monitor the folder home/pi/webcam/ for new images and then add a timedate to them
and copy them to the Mycloud server in the following folders:
\\WDMYCLOUD\werner\wernerterreblanche\webcam_latest
\\WDMYCLOUD\werner\wernerterreblanche\webcam_backup


You will need to add a symbolic link to the location where the latest photo files are stored.
ln -s /home/pi/webcam_latest /var/www/html/webcam_latest

You will also need a symbolic link from www to the html file:
ln -s /home/pi/scripts/python/camera.html /var/www/html/camera.html

# python
###### example of how to run the watch script:
'python /home/pi/scripts/python/watch_for_changes.py /mnt/mycloud/wernerterreblanche/webcam'


You will need to modify the crontab on the RPi to include the following:
*/5 * * * * /home/pi/scripts/python/start_runwatch.sh >> /home/pi/scripts/python/start_runwatch.log 2>&1
*/15 * * * * /home/pi/scripts/python/backup.sh >> /home/pi/scripts/python/backup.log 2>&1



