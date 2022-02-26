# Challenge 1:
### Game selects a random action for the user to do and displays the corresponding Image for it

Let’s start with three basic actions: 
- Clicking Button A, Clicking Button B or flipping the Micro:bit<br>
For each action:
- Create an image 
- Store each image in a variable
- Store all images in a list

--------------------------------------------------------

# Challenge 2:
### Game selects a random action for the user to do and displays the corresponding Image for it
  - Given the list of actions, the game needs to randomly select one of them 
  - Import the random library to access its functions
  - Look through documentation to find a function that can generate a random number between two values
  - Call the function using arguments that will give you a random number between the first and last indexes of the actions list
  - Store the random number in a variable. This will be the index of the action that has been selected
  - Display the current action using the index

--------------------------------------------------------

# Challenge 3:
### Game checks to see if the player accomplished the task within the timeframe: 
  - Find a function in the Micro:bit library that returns the amount of time that has passed since the start of the program. We can use this to create a timer for our game. 
  - Declare a variable to keep track of time and initialize it with the length of time given for each action. (Remember: 1 second = 1000 milliseconds)

--------------------------------------------------------

# Challenge 4:
### Write a conditional statement that checks if the player is still within the timeframe allocated for the action
  - If the time allowed minus the running time of the program is greater than zero, then the player still has time to complete the action

Example:
  - If the player has 3000 milliseconds (or 3 seconds) to complete the action and the program has been running for 2000 milliseconds, then there is still 1000 milliseconds to complete the action

--------------------------------------------------------

# Challenge 5:
### If time is not up and the user finishes the task, increase the score and select the next task
  - Add a set of conditionals within your current if statement that checks if the player completed the action:
    1) The action is completed if an action, such as a button press, is detected and matches the index of the image is corresponds to in the list we created earlier
    2) If they match, increase the score variable

--------------------------------------------------------

# Challenge 6:
### If time is up, the game is over.
  - Add another statement to your conditional, where if the game is over:
    - Display the score
    
--------------------------------------------------------


