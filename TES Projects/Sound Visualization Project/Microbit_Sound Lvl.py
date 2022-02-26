# Add your Python code here. E.g.
from microbit import *

#Volume level for LED lights from dead quiet to very_loud 
dead_quiet = "00000"
quiet = "90000"
lil_loud = "99000"
quite_loud = "99900"
loud = "99990"
very_loud = "99999"
#Colon variable created for the sake of using the join method (easier to cocatenate the variables for Image)
colon = ":"

#Starts off with a list containing an image representation of no LED lights on
vol_display = [dead_quiet, dead_quiet, dead_quiet, dead_quiet, dead_quiet]
while True:
    #microphone.sound_level used detect sound pressure level and returns a val b/w 0-255
    sound_lvl = microphone.sound_level()
    
    #display.scroll(sound_lvl)
    
    #If and elif conditions created to detect 5 different points of sound pressure lvl
    #Pops off the first element in the vol_display list and appends the respective variable
    #Since the Microbit contains 5 rows.
    if sound_lvl > 0 and sound_lvl < 20:
        #display.scroll("Quiet")
        vol_display.pop(0)
        vol_display.append(quiet)
    elif sound_lvl >= 20 and sound_lvl < 45:
        #display.scroll("A lil louder")
        vol_display.pop(0)
        vol_display.append(lil_loud)
    elif sound_lvl >= 45 and sound_lvl < 70:
        #display.scroll("Quite loud")
        vol_display.pop(0)
        vol_display.append(quite_loud)
    elif sound_lvl >= 70 and sound_lvl < 90:
        #display.scroll("Loud")
        vol_display.pop(0)
        vol_display.append(loud)
    elif sound_lvl >= 90:
        #display.scroll("Very loud")
        vol_display.pop(0)
        vol_display.append(very_loud)
        
    
    #Displays the new image on the microbit following the popping and appending from the if/elif conditions
    display.show(Image(colon.join(vol_display)))

    #Pause on that image representation for 100 milliseconds before looping
    sleep(100)
        