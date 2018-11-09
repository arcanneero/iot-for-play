import RPi.GPIO as GPIO
import compteur
import api

GPIO.setmode(GPIO.BCM)

api_conf = {"host" : 'localhost',
            "port" : 8080,
            "base" : '/compteur'
            }
gpio_compteur = [{"pin":18, "id":1},
                 {"pin":25, "id":2},
                 {"pin":2, "id":3},
                 {"pin":9, "id":4}]
debug = False

api.init(api_conf, debug)
compteur.init(gpio_compteur, debug)
