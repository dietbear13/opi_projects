import OPi.GPIO as GPIO
import time
import orangepi.pi3b

GPIO.setmode(orangepi.pi3b.BOARD)
TRIG_OUT = 12
ECHO_IN = 3
red_light = 11

# # Пины для TRIG и ECHO
# TRIG = GPIO.setup(TRIG_OUT, GPIO.OUT, initial=GPIO.HIGH)  # Пин 12
# ECHO = GPIO.GPIO4_A1  # Пин 16
# # Инициализация GPIO

GPIO.setwarnings(False)
GPIO.setup(TRIG_OUT, GPIO.OUT, initial=1)
GPIO.setup(ECHO_IN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(red_light, GPIO.OUT, initial=0)


def get_distance():
    GPIO.output(TRIG_OUT, 1)
    time.sleep(0.00001)  # 10 мкс
    # GPIO.output(TRIG_OUT, 0)
    # Ожидаем ответа
    while GPIO.input(ECHO_IN) == 0:
        # GPIO.output(red_light, 0)
        start_time = time.time()
        if GPIO.input(ECHO_IN) == 1:
            stop_time = time.time()
            return start_time, stop_time
    # sleep(2)
    # while GPIO.input(ECHO_IN) == 1:
    #     GPIO.output(red_light, 1)
    #     stop_time = time.time()
    #     break


    print(f'start_time {start_time}')
    # Расчет расстояния
    elapsed_time = stop_time - start_time
    print('start_time', start_time)
    print('stop_time', stop_time)
    distance = round(elapsed_time * 340, 2)
    print('Distanse', distance)
    return distance
try:
    while True:
        distance = get_distance()
        GPIO.output(TRIG_OUT, 1)
        print(f"Расстояние: {distance:.2f} см")
        time.sleep(1)
except KeyboardInterrupt:
    print('Error')
    GPIO.cleanup()

