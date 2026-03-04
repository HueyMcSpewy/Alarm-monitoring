import RPi.GPIO as GPIO
import time

testingpinbcm= 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(testingpinbcm, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    test = GPIO.input(testingpinbcm)
    if test == 1:
        print("nc")
    else:
        print("no")
    time.sleep(0.3)
