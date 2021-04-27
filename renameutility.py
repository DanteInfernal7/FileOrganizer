import os, glob

from filesorting import currentDir
from loggenerator import *



class renameUtil():
    def __init__(self,current,changed):
        self.current = current
        self.changed = changed

    def renameSingle(self):
        for file in os.scandir():
            if file.is_dir() or file == "<DirEntry 'log.txt'>":
                continue
            else:
                ext = os.path.splitext(self.current[0])
                os.rename(self.current[0],self.changed+ext[1])
                addtoLog(currentDir,self.current[0],self.changed+ext[1])
                os.chdir(currentDir)
                f = open("Log\log.txt", "a")
                f.write("\n######## OPERATION COMPLETE ########\n")
                f.write("\n")
                f.close()
                break




    def renameBulk(self):
        allfiles = glob.glob('*')
        num = 1
        for file in os.scandir():
            if file.is_dir() or file == "<DirEntry 'log.txt'>":
                continue
            try:
                for select in allfiles:
                    if select in self.current:
                            ext = os.path.splitext(select)
                            os.rename(select, self.changed + str(num) + ext[1])
                            num = num + 1
                            addtoLog(currentDir,select+" renamed to "+self.changed + str(num) + ext[1])

            except:
                continue



        os.chdir(currentDir)
        f = open("Log\log.txt", "a")
        f.write("\n######## OPERATION COMPLETE ########\n")
        f.write("\n")
        f.close()