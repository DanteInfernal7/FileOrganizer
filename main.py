import os
from filesorting import *

currentDir = input("Select Folder: ")
os.chdir(currentDir)

# class MyApp(App):
#     def build(self):
#         return Label(text="File Sorter")
#
# if __name__ == "__main__":
#     MyApp().run()

filesort(currentDir)