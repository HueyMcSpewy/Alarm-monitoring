import time
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import logging
import requests

# dotenv
Pushoverkey = ""
pushovertoken = ""
mqttbroker = ""
mqttuser = ""
mqttpass = ""
armpin = 2
alarmpin = 3

#logging setup
logging.basicConfig(level=logging.INFO)

# gpio
GPIO.setmode(GPIO.BCM)
GPIO.setup(armpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(alarmpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# intial states
last_armed = None
last_triggered = None

# mqtt
client = mqtt.Client(client_id="ALARM-MONITOR", protocol=mqtt.MQTTv5)
client.username_pw_set(mqttuser, mqttpass)
client.connect(mqttbroker, 1883, 60)
client.loop_start()

# pushover
def send_pushover(title, message, priority=0):
    try:
        requests.post(
            "https://api.pushover.net/1/messages.json",
            data={
                "token": pushovertoken,
                "user": Pushoverkey,
                "title": title,
                "message": message,
                "priority": priority
            }
        )
    except Exception as e:
        print("Pushover error:", e)


try:
    # arm loop
    while True:
        armed = GPIO.input(armpin)
        alarm = GPIO.input(alarmpin)

        if armed != last_armed:
            last_armed = armed
            if armed == 0:
                send_pushover("System Armed", "Alarm system is now armed", -2)
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
        logging.info("loop")
        time.sleep(0.2)

finally:
    GPIO.cleanup()
