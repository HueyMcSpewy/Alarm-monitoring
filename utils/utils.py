import RPi.GPIO as GPIO
import logging
import time
import os
import paho.mqtt.client as mqtt

# Globals
last_armed = None
last_triggered = None
armpin = None
alarmpin = None
Pushoverkey = None
pushovertoken = None
mqttbroker = None
mqttuser = None
mqttpass = None
client = None

def start():
    global last_armed, last_triggered
    global armpin, alarmpin
    global Pushoverkey, pushovertoken
    global mqttbroker, mqttuser, mqttpass
    global client

    # Environment variables (load only once in main.py)
    Pushoverkey = os.getenv("PUSHOVER_KEY")
    pushovertoken = os.getenv("PUSHOVER_TOKEN")
    mqttbroker = os.getenv("MQTT_BROKER")
    mqttuser = os.getenv("MQTT_USER")
    mqttpass = os.getenv("MQTT_PASS")
    armpin = int(os.getenv("ARM_PIN"))
    alarmpin = int(os.getenv("ALARM_PIN"))

    # GPIO setup
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(armpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(alarmpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    last_armed = GPIO.input(armpin)
    last_triggered = GPIO.input(alarmpin)

    logging.info("GPIO LOADED")

    # MQTT setup
    client = mqtt.Client(client_id="ALARM-MONITOR")
    client.username_pw_set(mqttuser, mqttpass)
    client.connect(mqttbroker, 1883, 60)
    client.loop_start()

    logging.info("MQTT LOADED")
    logging.info("Setup loaded")
