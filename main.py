import RPi.GPIO as GPIO
from sys import exit
from time import sleep
from aliot.aliot import alive_iot as iot
from distance_sensor import DistanceSensor
from threading import Thread
from intersection import FourWayIntersection
from traffic_light import TrafficLight
from led import Led

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 

projectId = '50cd307b-a3d6-45a1-9664-b4178a96009c'
my_iot = iot.ObjConnecteAlive(object_id='0cc3f29e-422c-44d0-8f0c-62a8854f58bd')

sensor = DistanceSensor(24, 23)
led = Led(18)

def sensor_daemon():
    while True:
        distance = sensor.distance()
        if distance <= 10 and distance >= 0:
            print(f'Distance: {distance} cm')
        sleep(0.1)

t = Thread(target=sensor_daemon, daemon=True)
t.start()

try:
    while True:
        led.on()
        sleep(1)
        led.off()
        sleep(1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
    exit()
