from led import Led

class TrafficLight:
    def __init__(self, aliot_obj: object, aliot_id: str, red_led_pin: int, yellow_led_pin: int, green_led_pin: int):
        """
        A collection of three LEDs (red, yellow and green) used as a traffic light.

        :param red_led_pin: The red LED pin
        :param yellow_led_pin: The yellow LED pin
        :param green_led_pin: The green LED pin
        """
        self.aliot_obj = aliot_obj
        self.aliot_id = aliot_id
        self.state = 'off'
        self.red_led = Led(red_led_pin)
        self.yellow_led = Led(yellow_led_pin)
        self.green_led = Led(green_led_pin)
        self.identifier = None
        self.intersection = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state):
        self._state = new_state
        if self.aliot_obj != None:
            self.aliot_obj.update_component(self.aliot_id, new_state)

    def red(self) -> None:
        """Change traffic light to red"""
        self.red_led.on()
        self.yellow_led.off()
        self.green_led.off()
        self.state = 'red'

    def yellow(self) -> None:
        """Change traffic light to yellow"""
        self.red_led.off()
        self.yellow_led.on()
        self.green_led.off()
        self.state = 'yellow'

    def green(self) -> None:
        """Change traffic light to green"""
        self.red_led.off()
        self.yellow_led.off()
        self.green_led.on()
        self.state = 'green'

    def off(self) -> None:
        """Change traffic light to off"""
        self.red_led.off()
        self.yellow_led.off()
        self.green_led.off()
        self.state = 'off'
