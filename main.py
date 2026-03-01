import time
import RPi.GPIO as GPIO
import asyncio
import paho.mqtt.client as mqtt
import os
import logging
from dotenv import load_dotenv
load_dotenv()

import utils.utils as utils
from utils.pushover import send_pushover
from utils.utils import start


# main part

utils.start()

try:
    # arm loop
    while True:
        armed = GPIO.input(utils.armpin)
        alarm = GPIO.input(utils.alarmpin)

        if os.getenv("ARM_PIN") is None:
            raise RuntimeError("ARM_PIN not set in environment")
        if armed != last_armed:
            last_armed = armed
            if armed == 0:
                send_pushover("System Armed", "Alarm system is now armd", -2)
                logging.info("armed")
                client.publish("home/alarm/armed", "ON", retain=True)
            else:
                send_pushover("System Disarmed", "Alarm system is now disarmed", -2)
                logging.info("disarmed")
                client.publish("home/alarm/armed", "OFF", retain=True)
        if alarm != last_triggered:
            last_triggered = alarm
            if alarm == 0:
                send_pushover("System Alarm", "The alarm system has been set off", 1)
                logging.warning("alarm")
                client.publish("home/alarm/alarm", "ON", retain=True)
            else:
                send_pushover("System clear", "The alarm system is now clear", 0)
                logging.info("clear")
                client.publish("home/alarm/alarm", "OFF", retain=True)
        time.sleep(0.2)

finally:
    GPIO.cleanup()
       
