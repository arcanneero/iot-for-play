#!/usr/bin/env python2.7  

import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)  
  
# GPIO 23 & 17 set up as inputs, pulled up to avoid false detection.  
# Both ports are wired to connect to GND on button press.  
# So we'll be setting up falling edge detection for both  
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
  
# GPIO 24 set up as an input, pulled down, connected to 3V3 on button press  
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
  
# now we'll define two threaded callback functions  
# these will run in another thread when our events are detected  
def my_callback(channel):  
    print "falling edge detected on 17"  
  
def my_callback2(channel):  
    print "falling edge detected on 23"  
  
GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback, bouncetime=300)  
GPIO.add_event_detect(23, GPIO.FALLING, callback=my_callback2, bouncetime=300)  
  
try:  
    print "Waiting for rising edge on port 24"  
    GPIO.wait_for_edge(24, GPIO.RISING)  
    print "Rising edge detected on port 24. Here endeth the third lesson."  
  
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()  
