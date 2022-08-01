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

sensor = DistanceSensor(24, 23)

l = TrafficLight(16, 20, 21)

# try:
#     while True:
#         l.red()
#         sleep(1)
#         l.yellow()
#         sleep(1)
#         l.green()
#         sleep(1)
# except KeyboardInterrupt:
#     pass
# finally:
#     GPIO.cleanup()
#     exit()

def main():
    while True:
        l.red()
        sleep(1)
        l.yellow()
        sleep(1)
        l.green()
        sleep(1)

feu_intel.on_start(callback=main)

feu_intel.run()

GPIO.cleanup()
# exit()
