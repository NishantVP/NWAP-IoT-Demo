import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO21
GPIO.setup(19, GPIO.OUT)  #LED to GPIO19

try:
    while True:
         button_state = GPIO.input(21)
         if button_state == False:
             GPIO.output(19, True)
             print('Button Pressed...')
             time.sleep(0.2)
         else:
             GPIO.output(19, False)
except:
    GPIO.cleanup()