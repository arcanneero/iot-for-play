import RPi.GPIO as GPIO
import api

compteurs = []

def init(tab, debug):
    global compteurs
    compteurs = tab
    print(compteurs)

    for compteur in compteurs:
        print(compteur)
        GPIO.setup(compteur['pin'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(compteur['pin'], GPIO.RISING, callback=callCount, bouncetime=300)


def callCount(channel):
    print("callCount on " + str(channel) + " pin")
    print(compteurs)
    for compteur in compteurs:
        if compteur['pin'] == channel:
            api.call(compteur['id'])