import RPi.GPIO as GPIO

class Led:
    def __init__(self, pin: int):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
    
    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)