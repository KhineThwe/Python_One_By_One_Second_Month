#OS module in python
import os

current = os.getcwd()
print('Current working directory',current)
os.chdir('/Users/khine/Desktop/')
print(os.getcwd())
