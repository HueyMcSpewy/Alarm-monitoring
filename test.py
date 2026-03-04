import RPi.GPIO

test = GPIO.input(19)

if test == 1:
    print("nc")
else:
    print("no")
