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
    feu_intel,
    TrafficLight('N', 16, 20, 21),
    TrafficLight('W', 2, 3, 4),
    TrafficLight('S', 13, 19, 26),
    TrafficLight('E', 25, 8, 7),
    DistanceSensor(24, 23),
    DistanceSensor(14, 15),
    DistanceSensor(5, 6),
    DistanceSensor(27, 17),
)

def main():
    while True:
        pass

def end():
    GPIO.cleanup()

feu_intel.on_start(callback=main)
feu_intel.on_end(callback=end)
feu_intel.run()
