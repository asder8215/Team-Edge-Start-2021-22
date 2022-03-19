# Team Edge Start
In this repository, it contains some quizzes, exercises, and projects that were done while teaching 2021-22 Team Edge Start Students.

# Quizzes
These are the link to all the Kahoot quizzes we have done (a couple of other quizzes were done on CodeHS):
- ### [If Statements](https://create.kahoot.it/details/99542693-d3dc-4dfe-af81-17054151a681)
- ### [Arithmetic and Types](https://create.kahoot.it/share/team-edge-review-kahoot/f1a834ef-0a1a-41b9-87af-6a3cc201e1cb)

# Projects
Longer term projects that apply what we have been teaching into a real situation
- ## [Animation Project](/projects/animation/animation_project.py)
  - A basic animation of the Among Us ඞ character fading in and out. Press B button to play the animation forward (Fade in) and A button to play it backwards (Fade out).
- ## [Sound Visualization](/projects/sound-visualization/sound_visualization.py)
  - The microbit screen will react to sounds around it detected by the microphone. The screen shows a horizontal bar representing the sound level, where 1 pixel is very low sound and 5 pixels (max) is a very high sound.
- ## [Reaction Game](/projects/reaction-game/reaction_project.py)
  - Ever played Bop-it before? This project is similar. The microbit will display an action on the screen, and the player has to perform that action within the given time frame (3 seconds). If the player performs the right action they get points and a chance to do more actions. If not, the game ends and shows the score. [Instructions](projects/reaction-game/instructions.md) to how to make the game.
- ## [Servo](/projects/servo-intro/)
  - The Servo is a small motor that can rotate between 0 and 180 degrees. Most servos use 5 volts for power, but the servo we used is 3V since the Microbit can only go up to 3 volts. Use `pin_.write_analog(angle)`, where pin_ is the GPIO pin you are using (pin0, pin1, pin2) and 0 <= angle <= 180 (anything above 180 will have no effect).
  - ### [Moving the Servo with Buttons](/projects/servo-intro/control-buttons.py)
    - This script allows you to move the servo arm to any angle between 0 to 180 degrees using the A and B.
  - ### [Move the Servo to a position](/projects/servo-intro/automatic-rotation.py)
    - Using the buttons A and B, move the arm from a center position to a right-most (B) or left-most (A) position automatically. The arm will move back to its original position.
  - ### [Move the Servo with the Accelerometer](projects/servo-intro/control-accelerometer.py)
    - Just like moving the Servo arm with buttons, rotate the arm by also rotating the microbit body left or right. Uses Linear Interpolation to convert the value of the accelerometer position to an angle that the Servo can rotate to.