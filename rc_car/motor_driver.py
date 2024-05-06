import gpiod
import time

# Define the pins for the motor
MOTOR_DIR_PIN = 17  # GPIO pin for the motor direction
MOTOR_PWM_PIN = 18  # GPIO pin for the motor speed (PWM)

# Open the GPIO chip and get the lines
chip = gpiod.Chip('gpiochip4')
dir_line = chip.get_line(MOTOR_DIR_PIN)
pwm_line = chip.get_line(MOTOR_PWM_PIN)

# Request the lines for output
dir_line.request(consumer="MotorDir", type=gpiod.LINE_REQ_DIR_OUT)
pwm_line.request(consumer="MotorPWM", type=gpiod.LINE_REQ_DIR_OUT)

# Function to set the motor direction
def set_direction(direction):
    if direction == 'forward':
        dir_line.set_value(1)
    elif direction == 'backward':
        dir_line.set_value(0)
    else:
        print("Invalid direction. Please specify 'forward' or 'backward'.")

# Function to set the motor speed
def set_speed(speed):
    # Note: This is a placeholder. The gpiod library does not support PWM.
    # You will need to use a different library or method to control the PWM signal.
    pwm_line.set_value(speed)

try:
    while True:
        set_direction('forward')
        set_speed(1)
        time.sleep(1)
        set_direction('backward')
        set_speed(0)
        time.sleep(1)
finally:
    dir_line.release()
    pwm_line.release()
