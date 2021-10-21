# Import required libraries
import sys
import time
import RPi.GPIO as GPIO
import pygame.mixer
import threading

mode = GPIO.getmode()
GPIO.cleanup()

bPin1 = 17
bPin2 = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(bPin1, GPIO.OUT)
GPIO.setup(bPin2, GPIO.OUT)


def reverse():
	time.sleep(2)
	GPIO.output(bPin1, GPIO.HIGH)
	GPIO.output(bPin2, GPIO.HIGH)
	time.sleep(3)
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
	thread_2 = threading.Thread(target=reverse)

	thread_1.start()
	thread_2.start()
