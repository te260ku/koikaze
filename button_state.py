
import RPi.GPIO as GPIO
import time

buttonPin = 18
GPIO.setmode(GPIO.BCM)
led_state = False
old_input_state = True
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT)



while True:
        new_input_state = GPIO.input(buttonPin)
        if new_input_state == False and old_input_state == True:
                led_state = not led_state
                time.sleep(0.2)
                old_input_state = new_input_state
                if led_state == False:
                        msg = 'on'
                        print (msg)
                        GPIO.output(17, led_state)

                else:
                        msg = 'off'
                        print (msg)
                        GPIO.output(17, led_state)
GPIO.cleanup()            
