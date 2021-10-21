import sys
import time
import RPi.GPIO as GPIO
import pygame.mixer
import threading


GPIO.cleanup()

StepPinForward=20
StepPinBackward=26
bPin1 = 16
bPin2 = 19


GPIO.setmode(GPIO.BCM)
GPIO.setup(StepPinForward, GPIO.OUT)
GPIO.setup(StepPinBackward, GPIO.OUT)
GPIO.setup(bPin1, GPIO.OUT)
GPIO.setup(bPin2, GPIO.OUT)



def motor():
     time.sleep(6)
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
     time.sleep(1)
     GPIO.cleanup()


def sound():
    pygame.mixer.init()
    pygame.mixer.music.load("./assets/walk.mp3")
    pygame.mixer.music.play(1)
    time.sleep(15)
    pygame.mixer.music.stop()


def main():
    thread_1 = threading.Thread(target=sound)
    thread_2 = threading.Thread(target=motor)

    thread_1.start()
    thread_2.start()

GPIO.cleanup()