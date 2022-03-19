from microbit import *

#                                                          -1024 <= x <= 1024                                  0 <= y <= 180
# uses Linear Interpolation to convert numbers in range from_low <= x <= from_high to the number in range to_low <= y <= to_high
def convert_angle(x, from_low, from_high, to_low, to_high):
    return (x - from_low) / (from_high - from_low) * (to_high - to_low) + to_low

while True:
    x_rotation = accelerometer.get_x()

    if -1024 <= x_rotation <= 1024:
        angle = convert_angle(x_rotation, -1024, 1024, 0, 180)
        pin0.write_analog(angle)
        print(angle)
        sleep(100)