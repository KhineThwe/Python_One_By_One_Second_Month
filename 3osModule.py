#OS module in python
import os
os.chdir('/Users/khine/Desktop/')
# os.mkdir('OS-Demo-2')
# os.makedirs('OS-Demo-3/Sub-Dir-1')
print(os.listdir())
#deleting folder
#for mkdir
# os.rmdir('OS-Demo-2')

#for makedirs
os.removedirs('OS-Demo-3/Sub-Dir-1')
print(os.listdir())
