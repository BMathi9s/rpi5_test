# main.py
from motor_driver import MotorDriver
from pyPS4Controller.controller import Controller

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        self.motor1 = MotorDriver(17, 18)
        self.motor2 = MotorDriver(22, 27)

    def on_left_stick_y_axis(self, value):
        speed = value / 32768
        direction = 1 if speed >= 0 else 0
        self.motor1.set_speed(abs(speed))
        self.motor1.set_dir(direction)

    def on_right_stick_y_axis(self, value):
        speed = value / 32768
        direction = 1 if speed >= 0 else 0
        self.motor2.set_speed(abs(speed))
        self.motor2.set_dir(direction)

def main():
    controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
    controller.listen()

if __name__ == "__main__":
    main()
