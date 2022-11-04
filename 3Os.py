#Os
import os
def current_path():
    print("Current Working Directory Before")
    print(os.getcwd())
current_path()
os.chdir('../')
current_path()
