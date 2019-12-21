# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
#GPIO.setmode(GPIO.BCM)
mode=GPIO.getmode()

GPIO.cleanup()

# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24

StepPinForward=26
StepPinBackward=20
bPin1 = 19
bPin2 = 16
sleeptime=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(StepPinForward, GPIO.OUT)
GPIO.setup(StepPinBackward, GPIO.OUT)
GPIO.setup(bPin1, GPIO.OUT)
GPIO.setup(bPin2, GPIO.OUT)

def forward(x):
    GPIO.output(StepPinForward, GPIO.LOW)
    GPIO.output(StepPinBackward, GPIO.HIGH)
    GPIO.output(bPin1, GPIO.LOW)
    GPIO.output(bPin2, GPIO.HIGH)
    print ("forwarding running  motor")
    time.sleep(x)
    # GPIO.output(StepPinForward, GPIO.LOW)
    # GPIO.output(bPin1, GPIO.LOW)

def reverse(x):
    GPIO.output(StepPinForward, GPIO.HIGH)
    GPIO.output(StepPinBackward, GPIO.LOW)
    GPIO.output(bPin1, GPIO.HIGH)
    GPIO.output(bPin2, GPIO.LOW)
    print ("backwarding running motor")
    time.sleep(x)
    # GPIO.output(StepPinBackward, GPIO.LOW)
    # GPIO.output(bPin2, GPIO.LOW)

print ("forward motor")
forward(5)
print ("reverse motor")
reverse(5)

print ("Stopping motor")
GPIO.cleanup()
