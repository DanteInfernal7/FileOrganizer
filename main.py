import os
import tkinter
from pathlib import Path
from tkinter import *
from tkinter import filedialog

from filesorting import *
from renameutility import *

def getDir():
    currentDir = filedialog.askdirectory()
    currentDir = currentDir.replace("/","\\")
    os.chdir(currentDir)
def singleRename(filenames,change):
    object = renameUtil(filenames,change)
    object.renameSingle()

def bulkRename(filenames,change):
    object = renameUtil(filenames, change)
    object.renameBulk()

def renameFunc(currentDir):
    filenames = []
    top = Toplevel()
    top.title("Rename Activity")
    title = Label(root, text="File Sorter")
    current = filedialog.askopenfilenames(initialdir=currentDir)
    changed = Entry(top)
    for file in current:
        temp = Path(file)
        filenames.append(temp.name)
    print(filenames)
    single = Button(top, text="Single Rename", command=lambda: singleRename(filenames,changed.get()))
    bulk = Button(top, text="Bulk Rename", command=lambda: bulkRename(filenames,changed.get()))
    title.grid(row=0, column=0)
    changed.grid(row=1, column=0)
    single.grid(row = 2, column=0)
    bulk.grid(row=2, column=1)




root = Tk()
# canvas = tkinter.Canvas(root,width = 720,height=1280)
root.title("File Sorter")
title = Label(root,text="File Sorter")
select = Button(root,text="Select a folder: ",command= lambda : getDir())
sort = Button(root,text="Sort",padx=20,command= lambda : filesort(currentDir))
rename = Button(root,text="Rename",command=lambda : renameFunc(currentDir))

title.grid(row=0,column=0)
select.grid(row=1,column=0)
sort.grid(row=2,column=0)
rename.grid(row=2,column=1)

root.mainloop()