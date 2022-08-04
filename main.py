import RPi.GPIO as GPIO
from sys import exit
from time import sleep
from aliot.aliot_obj import AliotObj
from distance_sensor import DistanceSensor
from intersection import FourWayIntersection
from traffic_light import TrafficLight

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 

feu_intel = AliotObj("feu-intel-v2")

intersection = FourWayIntersection(
    TrafficLight(feu_intel, 'lum', 16, 20, 21),
    None,
    None,
    None,
    DistanceSensor(24, 23),
    None,
    None,
    None,
)

def main():
    while True:
        pass

def end():
    GPIO.cleanup()

feu_intel.on_start(callback=main)
feu_intel.on_end(callback=end)
feu_intel.run()
