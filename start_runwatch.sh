#!/bin/sh
date
result=`ps -efd | grep watch_for_changes.py | grep -v "grep" | wc -l`
if [ $result -ge 1 ]
   then
        # Python script is already running. Kill its process
        /usr/bin/python /home/pi/projects/cameramon/killPython.py watch_for_changes.py
fi
result=`ps -efd | grep watch_for_changes.py | grep -v "grep" | wc -l`
if [ $result -eq 0 ]
    then
        cd /home/pi/projects/cameramon/
        /home/pi/projects/cameramon/runwatch.sh &
fi
