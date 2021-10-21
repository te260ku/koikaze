import RPi.GPIO as GPIO

ledPin = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(ledPin, GPIO.OUT)

def ledon():
	GPIO.output(ledPin, GPIO.HIGH)
	print ('ON')
def ledoff():
	GPIO.output(ledPin, GPIO.LOW)
	print ('OFF')
