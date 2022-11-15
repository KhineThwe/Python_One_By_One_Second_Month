#OS module in python
import os
from datetime import datetime
os.chdir('/Users/khine/Desktop/')
# os.makedirs('OS-Demo-2/Sub-Dir-1')
# os.rename('test.txt','demo.txt')
print(os.stat('demo.txt').st_size)
print(os.stat('demo.txt').st_mtime)

mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))
print(os.listdir())

