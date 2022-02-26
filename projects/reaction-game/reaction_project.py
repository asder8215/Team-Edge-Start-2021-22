# Add your Python code here. E.g.
from microbit import *
import random

left_button = Image("00900:"
                    "09000:"
                    "90000:"
                    "09000:"
                    "00900")
right_button = Image("00900:"
                    "00090:"
                    "00009:"
                    "00090:"
                    "00900")
flip = Image("99999:"
             "90009:"
             "90909:"
             "09999:"
             "00900")

actions = [left_button, right_button, flip]
action_image = actions[random.randint(0, 2)]
#3000 ms --> 3 seconds
timer = 3000
score = 0

def nextAction():
    #score is a global variable that the function can
    #access now
    global score
    global timer
    global action_image
    #Same as score = score + 1
    score += 1
    action_image = actions[random.randint(0, 2)]
    display.show(action_image)
    timer = 3000 + running_time()

while True:
    display.show(action_image)
    #It actively checks the time that the microbit is running for
    if timer > running_time():
        if button_a.is_pressed() and action_image == actions[0]:
            nextAction()
        elif button_b.is_pressed() and action_image == actions[1]:
            nextAction()
        elif accelerometer.current_gesture() == "face down" and action_image == actions[2]:
            nextAction()
    else:
        display.scroll("GAME OVER Score: " + str(score))
        break # added after so no infinite loop