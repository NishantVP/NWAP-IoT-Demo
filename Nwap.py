#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import time
import requests
import json
import datetime

# Init
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(40,GPIO.OUT)

continue_reading = True

# url = 'http://10.0.0.54:3000/attendance'
urlLocal = 'http://10.0.0.54:3000/changeVideo'
urlEC2 = 'http://ec2-54-219-158-77.us-west-1.compute.amazonaws.com:3000/changeVideo'
headers = {'Content-Type': 'application/json'}

# END Init

# Functions Def
def sendPOSTRequest(rfidTag):

    # data = '''{"date":"07/05/2016","day":"wednesday","rfid":''' +str(rfidTag) +'''}'''
    url = urlEC2
    print("Sending POST request...")
    data = '''{"name":"Nishant","color":"blue","rfid":"''' +str(rfidTag) +'''"}'''
    # print data
    response = requests.post(url, headers=headers ,data=data)
    print response

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# END Functions Def

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

timeNow = datetime.datetime.now()
f = open("Logs.txt","a") #opens file with name of "test.txt"
f.write(" \n------- New Session -------\n");
f.write( '---- Time = ' + repr(timeNow) + '-----\n' );
f.close();

# Welcome message
print "Welcome to the NWAP IoT Demo"
print "Press Ctrl-C to stop."


lastUID = ""
# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:

    # Scan for cards
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"

    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        currentUID = str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])

        if currentUID == lastUID:
            print "same card detected"
            time.sleep(1)
            print "UID Reset Success"
            lastUID = ""

        else:
            lastUID = currentUID
            # Print UID
            print "Card read UID: " +currentUID

            sendPOSTRequest(currentUID);

            print "Writting to file... "
            f = open("Logs.txt","a") #opens file with name of "test.txt"
            f.write( '---- RFID = ' + repr(currentUID) + '-----\n' );
            f.close();

            print "LED on"
            GPIO.output(40,GPIO.HIGH)
            time.sleep(1)

            print "LED off"
            GPIO.output(40,GPIO.LOW)

            # This is the default key for authentication
            key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]

            # Select the scanned tag
            MIFAREReader.MFRC522_SelectTag(uid)