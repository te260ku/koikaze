import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

buttonPin = 18
ledPin = 17
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

led_state = False
old_input_state = True

while True:
	new_input_state = GPIO.input(buttonPin)
	if new_input_state == False and old_input_state == True:
		led_state = not led_state
		time.sleep(0.2)
	old_input_state = new_input_state
	GPIO.output(ledPin, led_state)
GPIO.cleanup()
