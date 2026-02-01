import network
import time
import urequests
from machine import Pin
from config import ssid, password, pushoverenbl, token, alarmpin, armpin, mserver, mclientid, armtopic, alarmtopic, userkey 

# Internal pullups 

alarmpin_obj = Pin(alarmpin, Pin.IN Pin.PULL_UP)
armpin_obj = Pin(armpin, Pin.IN Pin.PULL_UP)


def arm_pin(alarmpin):
    if alarmpin.value() == 0:
# come back with mqtt and pushover
        pass
    else:
        pass

def wifi(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to network")
        sta_if
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print("network config", sta_if.ifconfig())

def pushover(pushoverenbl, token, userkey, title, message):
    if pushoverenbl == True:
        data = {
            "token": {token},
            "user": {userkey},
            "title": {title},
            "message": {message}
        }