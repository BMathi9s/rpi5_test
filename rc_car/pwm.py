import gpiod
import time

# Define the chip and line
chip = gpiod.Chip('gpiochip0')
line = chip.get_line(12)  # Use GPIO12 (pin 32 on the Pi)

# Define the PWM parameters
frequency = 1000  # Frequency in Hz
duty_cycle = 0.5  # Duty cycle (0.0 <= dc <= 1.0)

# Create a PWM line
line.request(consumer='my_app', type=gpiod.LINE_REQ_EV_PULSE, flags=gpiod.LINE_REQ_FLAG_ACTIVELOW)
line.set_config(0, gpiod.LINE_REQ_FLAG_ACTIVELOW, gpiod.LINE_REQ_EV_PULSE)

# Set the PWM parameters
line.set_pwmcycle(frequency, duty_cycle)

# Enable the PWM
line.enable()

# Wait for a while
time.sleep(10)

# Disable the PWM
line.disable()
