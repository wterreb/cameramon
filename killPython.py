import sys
import psutil
import os

# This will kill a running Python script

def kill_python_script(name):
        processes = filter(lambda p: psutil.Process(p).name() == "python", psutil.pids())

        scripts = []
        paths = []
        for pid in processes:
            try:
                #scripts.append(psutil.Process(pid).cmdline()[1])
                scriptname = psutil.Process(pid).cmdline()[1]
                if name in scriptname:
                     print ("Killing : " + scriptname);
                     p = psutil.Process(pid)
                     p.kill()
                     return True;
            except IndexError:
                pass
        print("Python script '" + scriptname + ' not running');
        return False;


if __name__ == '__main__':
        args = sys.argv[1:]
        PROCNAME = args[0] if args else 'INVALID USAGE'
        kill_python_script(PROCNAME)  # Looking if Python script is running and kill it if true





