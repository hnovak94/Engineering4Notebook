
# Online Python - IDE, Editor, Compiler, Interpreter
# Automatic Dice Roller
# Written by Harriet

import random 
from random import randint
print ("Automatic Dice Roller") # prints at top
min = 1 # smallest number on the die
max = 6 # largest number on the die
roll_again = "yes" # typing yes triggers code reset

while roll_again == "yes": # if yes is typed (see bottom) then print and give value
    print ("rolling dice...") # prints 'rolling dice'
    print (random.randint(min, max)) # prints randomized number between 1 and 6

    roll_again = input("roll dice again?") # waiting for input "yes"
