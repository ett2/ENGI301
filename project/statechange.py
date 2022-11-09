import Adafruit_BBIO.GPIO as GPIO
import time

# This does a few things:
# - Takes state information from the RF radio
# - Takes emergency braking information from both ultrasonic sensors
# - Combines both signals to determine final signal
# - Outputs final states to be outputted to Jetson


def statechange(rf_state, ultrasonic_state):
    final_state = 0;
    if ultrasonic_state == True:
        final_state = 4
    else:
        final_state = rf_state
    return final_state