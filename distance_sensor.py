import RPi.GPIO as GPIO
from time import time, sleep
from threading import Thread

MICROSECOND = 0.000001

class DistanceSensor:
    def __init__(self, trig_pin: int, echo_pin: int):
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin
        self.direction = None
        self.intersection = None
        GPIO.setup(self.trig_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)
        t = Thread(target=self.__sensor_daemon, daemon=True)
        t.start()

    def __sensor_daemon(self):
        while True:
            distance = self.distance()
            if distance <= 10 and distance >= 0:
                print(f'Distance: {distance} cm')
                self.intersection.update(self)
            sleep(0.1)

    def distance(self):
        try:
            GPIO.output(self.trig_pin, GPIO.HIGH)
            sleep(10 * MICROSECOND)
            GPIO.output(self.trig_pin, GPIO.LOW)
        
            while GPIO.input(self.echo_pin) == 0:
                pulse_start_time = time()
            while GPIO.input(self.echo_pin) == 1:
                pulse_end_time = time()
        
            pulse_duration = pulse_end_time - pulse_start_time
            distance = round(pulse_duration * 17150, 2)

            return distance
        except:
            return -1
