import os, glob

getDir = input("Select Folder: ")
os.chdir(getDir)

class renameUtil():
    def __init__(self,current,changed):
        self.current = current
        self.changed = changed

    def renameSingle(self):
        for file in os.scandir():
            if file.is_dir() or file == "<DirEntry 'log.txt'>":
                continue
            else:
                os.rename(self.current,self.changed)
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
            except:
                continue

obj1 = renameUtil("test.txt","test1.txt")
obj1.renameSingle()
arr = ["1.txt","2.txt","3.txt","4.txt","5.txt","6.txt"]
obj2 = renameUtil(arr,"success")
obj2.renameBulk()


