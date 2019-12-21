# Import required libraries
import sys
import time
import RPi.GPIO as GPIO
import pygame.mixer
import threading

# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24
GPIO.cleanup()

StepPinForward=26
StepPinBackward=20
bPin1 = 19
bPin2 = 16


GPIO.setmode(GPIO.BCM)
GPIO.setup(StepPinForward, GPIO.OUT)
GPIO.setup(StepPinBackward, GPIO.OUT)
GPIO.setup(bPin1, GPIO.OUT)
GPIO.setup(bPin2, GPIO.OUT)



def motor():
     time.sleep(3)
     GPIO.output(StepPinForward, GPIO.HIGH)
     GPIO.output(StepPinBackward, GPIO.LOW)
     GPIO.output(bPin1, GPIO.HIGH)
     GPIO.output(bPin2, GPIO.LOW)
     # print "backwarding running motor"
     time.sleep(4)
     GPIO.output(StepPinForward, GPIO.LOW)
     GPIO.output(StepPinBackward, GPIO.LOW)
     GPIO.output(bPin1, GPIO.LOW)
     GPIO.output(bPin2, GPIO.LOW)
     time.sleep(3)
     GPIO.cleanup()

def sound():
    pygame.mixer.init()
    pygame.mixer.music.load("walk.mp3")
    pygame.mixer.music.play(1)
    time.sleep(20)
    pygame.mixer.music.stop()

def main():

    thread_1 = threading.Thread(target=sound)
    thread_2 = threading.Thread(target=motor)

    thread_1.start()
    thread_2.start()

main()
GPIO.cleanup()
