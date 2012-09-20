#!/usr/bin/python
from Adafruit_CharLCD import Adafruit_CharLCD
import RPi.GPIO as GPIO
from subprocess import * 
from time import sleep, strftime
from datetime import datetime
import tweepy
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("config.ini")

CONSUMER_KEY = Config.get('TwitterAppTokens','CONSUMER_KEY')
CONSUMER_SECRET = Config.get('TwitterAppTokens','CONSUMER_SECRET')
OAUTH_TOKEN = Config.get('TwitterAppTokens','OAUTH_TOKEN')
OAUTH_SECRET = Config.get('TwitterAppTokens','OAUTH_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN,OAUTH_SECRET)
api = tweepy.API(auth)

statuses = api.user_timeline()

LED_PIN=4
BUTTON_PIN=18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN)

lcd = Adafruit_CharLCD()
status_index = 0

def updateLcd():
	print "updated!!"+str(status_index+1)
	lcd.clear()
	sleep(0.4)
	lcd.message("Reading Tweet "+str(status_index+1))
	sleep(1)
	lcd.clear()
	sleep(0.5)
	lcd.message(str(statuses[status_index].created_at)+'\n'+statuses[status_index].text)


lcd.begin(16,1)
updateLcd()
while 1:
	sleep(0.3)
	lcd.scrollDisplayLeft()
	if GPIO.input(BUTTON_PIN)==False:
		print "Clicked!"
		status_index += 1 
		updateLcd()

