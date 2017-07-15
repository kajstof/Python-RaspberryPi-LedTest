import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
while True:
    print("LED (GPIO 18 Port): On")
    GPIO.output(18, GPIO.HIGH)
    time.sleep(1)
    print("LED(GPIO 18 Port): Off")
    GPIO.output(18, GPIO.LOW)
    time.sleep(1)
