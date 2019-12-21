# Import required libraries
import sys
import time
import RPi.GPIO as GPIO
import pygame.mixer
import threading

# Use BCM GPIO references
# instead of physical pin numbers
#GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24



GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)


GPIO.output(16, GPIO.HIGH)
GPIO.output(19, GPIO.HIGH)
GPIO.output(20, GPIO.HIGH)
GPIO.output(26, GPIO.HIGH)
# GPIO.cleanup()

