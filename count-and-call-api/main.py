import RPi.GPIO as GPIO
import compteur
import api

GPIO.setmode(GPIO.BCM)

api_conf = {"host" : 'localhost',
            "port" : 8080,
            "base" : '/compteur'
            }
gpio_compteur = [{"pin":14, "id":1},
                 {"pin":25, "id":2},
                 {"pin":2, "id":3},
                 {"pin":9, "id":4}]
debug = False

api.init(api_conf, debug)
compteur.init(gpio_compteur, debug)


# GPIO 24 set up as an input, pulled down, connected to 3V3 on button press
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    print "Waiting for rising edge on port 24"
    GPIO.wait_for_edge(24, GPIO.RISING)
    print "Rising edge detected on port 24. Here endeth the third lesson."

except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normale