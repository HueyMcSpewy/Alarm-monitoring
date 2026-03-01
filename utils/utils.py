from dotenv import load_dotenv
load_dotenv()

import RPi.GPIO as GPIO
import logging
import time
import os
import paho.mqtt.client as mqtt

load_dotenv()
Pushoverkey = os.getenv("PUSHOVER_KEY")
pushovertoken = os.getenv("PUSHOVER_TOKEN")
mqttbroker = os.getenv("MQTT_BROKER")
mqttuser = os.getenv("MQTT_USER")
mqttpass = os.getenv("MQTT_PASS")
armpin = int(os.getenv("ARM_PIN"))
alarmpin = int(os.getenv("ALARM_PIN"))

# Initial states
last_armed = None
last_triggered = None

client = mqtt.Client(client_id="ALARM-MONITOR")

def start():
    global last_armed, last_triggered

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(armpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(alarmpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    last_armed = GPIO.input(armpin)
    last_triggered = GPIO.input(alarmpin)

    logging.info("GPIO LOADED")

    client.username_pw_set(mqttuser, mqttpass)
    client.connect(mqttbroker, 1883, 60)
    client.loop_start()

    logging.info("MQTT LOADED")
    logging.info("Setup loaded")