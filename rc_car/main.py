# main.py
from motor_driver import MotorDriver
from pyPS4Controller.controller import Controller
import time

speed_c = 0.5

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        self.motor1 = MotorDriver(17, 18)
        self.motor2 = MotorDriver(22, 27)

    # def on_left_stick_y_axis(self, value):
    #     speed = value / 32768
    #     direction = 1 if speed >= 0 else 0
    #     self.motor1.set_speed(abs(speed))
    #     self.motor1.set_dir(direction)

    # def on_right_stick_y_axis(self, value):
    #     speed = value / 32768
    #     direction = 1 if speed >= 0 else 0
    #     self.motor2.set_speed(abs(speed))
    #     self.motor2.set_dir(direction)

    def on_up_arrow_press(self):
        self.motor1.set_speed(speed_c)
        self.motor1.set_dir(1)
        self.motor2.set_speed(speed_c)
        self.motor2.set_dir(1)

    def on_down_arrow_press(self):
        self.motor1.set_speed(speed_c)
        self.motor1.set_dir(0)
        self.motor2.set_speed(speed_c)
        self.motor2.set_dir(0)

    def on_left_arrow_press(self):
        self.motor1.set_speed(speed_c)
        self.motor1.set_dir(0)
        self.motor2.set_speed(speed_c)
        self.motor2.set_dir(1)

    def on_right_arrow_press(self):
        self.motor1.set_speed(speed_c)
        self.motor1.set_dir(1)
        self.motor2.set_speed(speed_c)
        self.motor2.set_dir(0)

    def on_up_down_left_right_arrow_release(self):
        self.motor1.set_speed(0)
        self.motor2.set_speed(0)
        time.sleep(5)

def main():
    controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
    controller.listen()

if __name__ == "__main__":
    main()
