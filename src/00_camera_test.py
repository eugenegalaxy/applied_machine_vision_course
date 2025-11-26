'''
Lecture 1: Introduction
Simple camera test for the Raspberry Pi Camera Module 3
If camera is connected and library is installed, this script will show a preview of the camera.
'''

from picamzero import Camera # install by running "sudo apt install python3-picamzero" in Terminal
from time import sleep


if __name__ == "__main__":
    camera = Camera()
    camera.start_preview()
    sleep(5) # Wait 5 seconds before closing the preview
