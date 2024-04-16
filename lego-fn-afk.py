import time
import os
import random
import subprocess
import threading

from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
from datetime import datetime


# runs the cls command in cmd prompt
os.system('cls')

# intro
print("")
print("This program is designed to farm xp while AFK in Lego Fortnite. Please make sure to tab into it.")
print("Press enter to continue, or type 'exit' to close the program.")
firstChoice = input("")

# if user inputs "exit"
if firstChoice == "exit":
    print("Cya!")
    time.sleep(2)
    exit()
else:
    # description and continuation of program
    print("=======================================================================")
    print("I will select a random number between 1 and 6, then wait that amount of minutes before sending inputs.")
    print("")
    print("I will simulate WASD, and I will Left Click using RSHIFT.")
    print("")
    print("You can stop me at any time by simply closing me.")
    print("")
    print("When tabbing out or closing me, you may need to tap shift, just to make sure it is no longer being 'pressed'.")
    print("")
    print("I will automatically close Fortnite and myself 5 hours after the main loop begins.")
    print("=======================================================================")
    print("")

    # generate the timestamp function for later use, will print as "[HH:MM:SS]"
    def generateTimestamp():
        now = datetime.now()
        return "[{}:{}:{}]".format(now.hour, now.minute, now.second)

    # program closes after 5 hours
    def programTimeout():
        time.sleep(18000) # 5hrs in seconds
        print("5 hours have passed. Shutting down...")
        time.sleep(3)
        subprocess.call(["taskkill","/F","/IM","FortniteClient-Win64-Shipping.exe"])
        time.sleep(2)
        os._exit(0)

    # determine if "minutes" should be pluralized based on the minutes variable
    def minutesPlural(minutes):
        if(minutes == 1):
            minPlural = "minute."
        else:
            minPlural = "minutes."
        return minPlural

    # final prompt before looping
    input("Press enter to start.")
    print("")
    print("Rolling the dice...")
    print("")

    # start the 5 hour timer in a different thread
    timeout_thread = threading.Thread(target=programTimeout)
    timeout_thread.start()

###########################################################################

    # main loop
    while True: 
        # define main vars, these numbers are in seconds
        minutes = random.randrange(1, 7) # btwn 1 and 6
        eatChance = random.randrange(1, 5) # btwn 1 and 4
        timeBtwnMoves = random.randrange(1, 3) # either 1 or 2
        wsMovement = random.randrange(1,3) # either 1 or 2

        plural = minutesPlural(minutes)

        print(generateTimestamp(), "Waiting", minutes , plural)#"minutes.")

        # convert chosen "minutes" into seconds for python
        time.sleep(minutes * 60) # adding )# to the end of "minutes" will revert the time.sleep back into seconds for debugging

        print(generateTimestamp(), "Moving...")

        # movement simulations
        simInput1 = press(key='A', sec=1) # Move left
        time.sleep(timeBtwnMoves)
        print(generateTimestamp(), "Jumping...")
        simInput3 = press(key='SPACEBAR', sec=1) # Jump
        #print(generateTimestamp(), "Moving...")
        simInput2 = press(key='D', sec=1) # Move right

        time.sleep(1)

        # 50% chance of moving either forward or backwards
        if(wsMovement == 1):
            simInput5 = press(key='W', sec=1)
            print(generateTimestamp(), "Moved forward...")
        elif(wsMovement != 1):
            simInput6 = press(key='S', sec=1)
            print(generateTimestamp(), "Moved backwards...")            
        
        time.sleep(1)

        # 1 in 4 chance the player will eat
        if(eatChance == 1):
            simInput4 = press(key='RSHIFT')
            print(generateTimestamp(), "Eating...")
        elif(eatChance != 1):
            print(generateTimestamp(), "Not eating...")
        
        # final print and loop
        time.sleep(1)
        print(generateTimestamp(), "Done!")
        print("")
        time.sleep(1)
        continue
        