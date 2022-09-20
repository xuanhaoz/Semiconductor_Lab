#from gpiozero import LED
import RPi.GPIO as GPIO

#gpio= LED(24)

#while True:
#    gpio.on()

GPIO.setmode(GPIO.BCM)

GPIO.setup(24,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
print("voltage on")

while True:
    GPIO.output(24,GPIO.HIGH)
    GPIO.output(23,GPIO.HIGH)