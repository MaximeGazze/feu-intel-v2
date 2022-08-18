import RPi.GPIO as GPIO
from sys import exit
from time import sleep
from distance_sensor import DistanceSensor
from intersection import FourWayIntersection
from traffic_light import TrafficLight

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 

l = TrafficLight(None, 'lum', 16, 20, 21)

# def main():
#     while True:
#         pass

def main():
    while True:
        l.red()
        sleep(1)
        l.yellow()
        sleep(1)
        l.green()
        sleep(1)

def end():
    GPIO.cleanup()

while True:
    main()
