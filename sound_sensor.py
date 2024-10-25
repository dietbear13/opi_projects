from time import sleep

import OPi.GPIO as GPIO
import orangepi.pi3b

GPIO.setmode(orangepi.pi3b.BOARD)

red_light = 11
green_light = 13
GPIO.setup(red_light, GPIO.OUT, initial=0)
GPIO.setup(green_light, GPIO.OUT, initial=0)

SOUND_SENSOR_PIN = 27
GPIO.setup(SOUND_SENSOR_PIN, GPIO.IN)

def detect_sound():
    sound_detected = GPIO.input(SOUND_SENSOR_PIN)
    print(sound_detected)
    if sound_detected == 1:
        GPIO.output(green_light, 1)
        print("Sound detected!")
        GPIO.output(green_light, 0)
    else:
        print("No sound", GPIO.input(SOUND_SENSOR_PIN))

try:
    while True:
        # sleep(0.1)
        detect_sound()
except KeyboardInterrupt:
    GPIO.cleanup()
