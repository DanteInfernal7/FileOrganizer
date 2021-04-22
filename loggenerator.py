import os
from datetime import datetime

def addtoLog(currentDir,log):
    if os.getcwd() != currentDir:
        os.chdir(currentDir)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    f = open("Log\log.txt", "a")
    f.write(current_time+" "+log+"\n")
    f.close()