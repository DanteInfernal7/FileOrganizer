import pathlib as path
import os

dirName = input("Select Folder to sort: ")
os.chdir(dirName)
class renameUtil():
    def __init__(self,current,changed):
        self.current = current
        self.changed = changed

    def renameSingle(self):
        for file in os.scandir():
            if file.is_dir():
                continue
    def renameBulk(self):
        for file in os.scandir():
            if file.is_dir():
                continue
    def rename(self):
        for file in os.scandir():
            if file.is_dir():
                continue



