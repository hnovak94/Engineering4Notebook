import random 
from random import randint

print ("Automatic Dice Roller") # prints at top
roll_again = "yes" # typing yes triggers code reset

side_number = input("number of sides?")
die_number = input("number of die?")
while roll_again != "x" : # if yes is typed (see bottom) then print and give value
    if roll_again == "c":
        side_number = input("number of sides?")
        die_number = input("number of die")
    min = 1 # smallest number on the die
    max =  int(side_number) # largest number on the die
    print ("rolling dice...") # prints 'rolling dice'
    for i in range(0, int(die_number)):
        print (random.randint(min, max)) # prints randomized number between 1 and 6

    roll_again = input("roll dice again?") # waiting for input "yes"
