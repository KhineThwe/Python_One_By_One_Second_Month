#OS module in python
import os
from datetime import datetime
os.chdir('/Users/khine/Desktop/')
#entire directories
for dirpath,dirnames,filenames in os.walk('/Users/khine/Desktop/'):
    print("Current Path: ",dirpath)
    print("Directories: ",dirnames)
    print("Files: ",filenames)

