raspberry-pi-GPIO
=================

This is my first Raspberry Pi GPIO project.
It's a simple twitter client, showing the user timeline in a text 16x2 LCD, I use a button to change to next tweet in the list. 
The script is Python, it uses also the twitter API.

First you need to creat a twitter app, see https://dev.twitter.com/apps/new
Then you should take your credentials, rename the file config.ini.dist to config.ini and enter your twitter app tokens in the file:

OAUTH_TOKEN=xxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxx
OAUTH_SECRET=xxxxxxxxxxxxxx
CONSUMER_KEY=xxxxxxxxxxxxxx
CONSUMER_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 

Now you need to setup your pyhton environment. 

You will need the folowing libs: 

RPi.GPIO - This is the library that comunicates with your raspberry pi thru gpio, if you already used arduino and the wiring language you will be familiar with this.

Tweepy - Python Twitter Library, basycaly it helps you with the authentication and twitter api.

I also used a lib from Adafruit, the Adafruit_CharLCD, this is for the LCD. This is the Adafruit_CharLCD.py file, no need to install.

To install RPI.GPIO and Tweepy I used pip.

Instaling Pip:

    $ sudo apt-get install python-setuptools
    $ sudo easy_install -U distribute
    $ sudo apt-get install python-pip

Installing libs with Pip:

    $ sudo pip install rpi.gpio
    $ sudo pip install tweepy

Wiring:
I used the Adafruit raspberry pi cobbler kit to easly connect the GPIO to a breadboard.
 
http://learn.adafruit.com/drive-a-16x2-lcd-directly-with-a-raspberry-pi/wiring

Later I'll upload the schematics.

Connect your GPIO and run the python script:

    $ sudo python gpio_lcd_twitter_client.py 

And you're done!
 
