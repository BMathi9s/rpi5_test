# main.py
from motor_driver import MotorDriver
from inputs import get_gamepad

def main():
    motor1 = MotorDriver(17, 18)  # create a MotorDriver object for the first motor
    motor2 = MotorDriver(22, 27)  # create a MotorDriver object for the second motor

    try:
        while True:
            events = get_gamepad()  # get the gamepad inputs
            for event in events:
                if event.code == 'ABS_Y':  # if the event is from the left joystick's Y-axis
                    speed = event.state / 32768  # normalize the joystick value to get a speed between 0 and 1
                    direction = 1 if speed >= 0 else 0  # determine the direction based on the sign of the speed
                    motor1.set_speed(abs(speed))  # set the speed of the first motor
                    motor1.set_dir(direction)  # set the direction of the first motor
                elif event.code == 'ABS_RZ':  # if the event is from the right joystick's Y-axis
                    speed = event.state / 32768  # normalize the joystick value to get a speed between 0 and 1
                    direction = 1 if speed >= 0 else 0  # determine the direction based on the sign of the speed
                    motor2.set_speed(abs(speed))  # set the speed of the second motor
                    motor2.set_dir(direction)  # set the direction of the second motor

    except KeyboardInterrupt:  # trap a CTRL+C keyboard interrupt
        motor1.set_speed(0)  # stop the first motor
        motor2.set_speed(0)  # stop the second motor

    finally:
        motor1.close()  # in case of unexpected exit, resets pin status (motor will go full speed after exiting)
        motor2.close()  # resets pin status

if __name__ == "__main__":
    main()
