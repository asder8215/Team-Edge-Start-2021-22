from microbit import *

ANGLE_UPPER = 180
ANGLE_START = 90
ANGLE_LOWER = 0
ANGLE_CHANGE = 5

pin0.write_analog(ANGLE_START)

while True:
    # move arm COUNTER-CLOCKWISE
    if button_a.is_pressed():
        for angle in range(ANGLE_START, ANGLE_UPPER, ANGLE_CHANGE):
            pin0.write_analog(angle)
            sleep(100)
        pin0.write_analog(ANGLE_START)
    # move arm CLOCKWISE
    elif button_b.is_pressed():
        for angle in range(ANGLE_START, ANGLE_LOWER, -ANGLE_CHANGE):
            pin0.write_analog(angle)
            sleep(100)
        pin0.write_analog(ANGLE_START)