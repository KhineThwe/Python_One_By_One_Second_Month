#OS module in python
import os
os.chdir('/Users/khine/Desktop/')
# print(os.environ.get("USERPROFILE"))#HOME
# print(os.getlogin())
file_path = os.path.join(os.environ.get("USERPROFILE"),'test.txt')
# print(file_path)
print(os.path.dirname('/Khine/tmp/test.mp3'))
print(os.path.basename('/tmp/test.mp3'))
print(os.path.split('/Khine/tmp/test.mp3'))
