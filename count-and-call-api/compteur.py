import RPi.GPIO as GPIO
import api

compteurs = []

def init(tab, debug):
    compteurs = tab

    for compteur in compteurs:
        GPIO.setup(compteur['pin'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(compteur['pin'], GPIO.RISING, callback=callCount, bouncetime=300)


def callCount(channel):
    print "callCount" + channel
    api.call(channel)
