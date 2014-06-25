#!/usr/bin/env python3
"""
This file will act as the base for the RasPiCam 

$ python CameraApp.py [delay]
"""
import dropbox, os, picamera, sys
from time import sleep

# setup
cam = picamera.PiCamera()


# Start a preview for any attatched screens
cam.start_preview()


def cam_loop(delay):
    try:
        for filename in cam.capture_continuous('iamge{counter}.jpg'):
            print(filename)
            sleep(delay)
            tweet_picture(filename)
            db_upload(filename)
            email_picture(filename)
            delete_picture(filename)

    finally:
        return

def tweet_picture():
    pass

def db_upload():
    pass

def email_picture():
    pass

def delete_picture():
    pass

if __name__ == "__main__":
    try:
        delay = sys.argv[1]
    except:
        delay = 60
    cam_loop(delay)
