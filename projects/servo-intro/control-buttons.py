from microbit import *

UPPER_LIMIT = 180
LOWER_LIMIT = 0
ANGLE_CHANGE = 5
angle = 0

while True:
    # button_a moves the servo arm COUNTER-CLOCKWISE
    if button_a.is_pressed() and angle <= UPPER_LIMIT:
        angle += ANGLE_CHANGE
        pin0.write_analog(angle)
    # button_a moves the servo arm CLOCKWISE
    elif button_b.is_pressed() and angle >= LOWER_LIMIT:
        angle -= ANGLE_CHANGE
        pin0.write_analog(angle) # only send signal when a button is pressed
    
    sleep(100)