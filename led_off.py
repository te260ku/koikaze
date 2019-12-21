# Import required libraries
import sys
import time
import RPi.GPIO as GPIO
import pygame.mixer
import threading

# Use BCM GPIO references
# instead of physical pin numbers
#GPIO.setmode(GPIO.BCM)
mode=GPIO.getmode()
GPIO.cleanup()

# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24

bPin1 = 17


GPIO.setmode(GPIO.BCM)

GPIO.setup(bPin1, GPIO.OUT)


GPIO.output(bPin1, GPIO.HIGH)
GPIO.cleanup()

