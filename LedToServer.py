import RPi.GPIO as GPIO
import time
import requests
import json

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO21
GPIO.setup(19, GPIO.OUT)  #LED to GPIO19

urlEC2 = 'http://ec2-54-193-96-90.us-west-1.compute.amazonaws.com:3000/changeState'
headers = {'Content-Type': 'application/json'}


# Functions Def
def sendPOSTRequest(state):

    url = urlEC2
    print("Sending POST request...")
    data = '''{"name":"Nishant","color":"red","state":"''' +str(state) +'''"}'''
    # print data
    response = requests.post(url, headers=headers ,data=data)
    print response


# Welcome message
print "Welcome to the NWAP IoT Demo"
print "Press Ctrl-C to stop."


try:
	while True:
		button_state = GPIO.input(21)
		if button_state == False:
			GPIO.output(19, True)
			print('Button Pressed...')
			sendPOSTRequest(True);
			time.sleep(2)
			sendPOSTRequest(False);
		else:
			GPIO.output(19, False)
except:
	GPIO.cleanup()