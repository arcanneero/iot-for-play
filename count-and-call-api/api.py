# coding=utf-8
import requests
import json
import time
import RPi.GPIO as GPIO

backend = {'api': 'http://localhost:8080/compteur',
         'delay': 60}
headers = {'content-type': 'application/json'}

def init(conf, debug):
    if conf['port'] == 80 :
        backend['api'] = 'http://' + conf['host'] + conf['base']
    else :
        backend['api'] = 'http://' + conf['host'] + ':' + str(conf['port']) + conf['base']

def get(url):
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        raise NameError(r.status_code)
    else:
        return r

def post(url, data):
    r = requests.post(url, json=data, headers=headers)
    if r.status_code != 200:
        raise NameError(r.status_code)
    else:
        return r

def put(url, data):
    r = requests.put(url, json=data, headers=headers)
    print(r.status_code)
    if r.status_code != 200:
        raise NameError(r.status_code)
    else:
        return r

def delete(url, data):
    r = requests.delete(url, json=data, headers=headers)
    if r.status_code != 200:
        raise NameError(r.status_code)
    else:
        return r

def getJson(url):
    body = get(url);
    try :
        return body.json()
    except:
        return body

def postJson(url, payload):
    body = post(url, payload);
    try :
        return body.json()
    except:
        return body

def putJson(url, payload):
    body = put(url, payload);
    try :
        return body.json()
    except:
        return body

def deleteJson(url, payload):
    body = delete(url, payload);
    try :
        return body.json()
    except:
        return body

def call(id):
    query_url = backend['api'] + id
    print(query_url)
    try:
        body = putJson(query_url, "{}")
        print(body)
    except :
        print("Erreur")
