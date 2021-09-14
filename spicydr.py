import random 
from random import randint

print ("Automatic Dice Roller") # prints at top
roll_again = "yes" # typing yes triggers code reset

side_number = input("number of sides?") # tell the roller the number of sides
die_number = input("number of die?") # tell the roller the number of die
while roll_again != "x" : # if yes is typed (see bottom) then print and give value
    if roll_again == "c": # use c as a command to exit loop, edit information
        side_number = input("number of sides?") # ask again number of sides
        die_number = input("number of die") # ask again number of die
    min = 1 # smallest number on the die
    max =  int(side_number) # largest number on the die, changes depending on side number
    # side_number (a string) must be converted into an integer
    print ("rolling dice...") # prints 'rolling dice'
    for i in range(0, int(die_number)): # loops as many times as the number of die used
    # die_number (a string) must be converted into an integer
        print (random.randint(min, max)) # prints randomized number between 1 and the side number

    roll_again = input("roll dice again?") # waiting for input "yes"
