import kivy
import os

import filesorting
from filesorting import *
from renameutility import *
from kivy.app import App
from kivy.uix.label import Label

dirName = input("Select Folder to sort: ")
os.chdir(dirName)

class MyApp(App):
    def build(self):
        return Label(text="File Sorter")

if __name__ == "__main__":
    MyApp().run()
    dirName = input("Select Folder to sort: ")
    os.chdir(dirName)
