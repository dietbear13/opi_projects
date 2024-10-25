from time import sleep

import OPi.GPIO as GPIO
import orangepi.pi3b

GPIO.setmode(orangepi.pi3b.BOARD)

red_light = 13
green_light = 11
blue_light = 15

# GPIO.setup(green_light, GPIO.OUT)
# GPIO.setup(red_light, GPIO.OUT)
# GPIO.setup(blue_light, GPIO.OUT)

try:
    GPIO.setup(red_light, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(green_light, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(blue_light, GPIO.OUT, initial=GPIO.LOW)
    sleep(5)
    GPIO.output(blue_light, GPIO.HIGH)
    for i in range(20):
        print(i,  i % 2 == 0,  i % 3 == 0,  i % 5 == 0)
        sleep(2)
        GPIO.output(green_light, i % 2 == 0 if GPIO.HIGH else GPIO.LOW)
        GPIO.output(blue_light, i % 3 == 0 if GPIO.HIGH else GPIO.LOW)
        GPIO.output(red_light, i % 5 == 0 if GPIO.HIGH else GPIO.LOW)

    GPIO.output(green_light, GPIO.HIGH)
    GPIO.output(blue_light, GPIO.HIGH)
    GPIO.output(red_light, GPIO.HIGH)
except Exception as e:
    print(e)
