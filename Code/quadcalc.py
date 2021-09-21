# Python Program 02 - Quadratic Solver (ENGR4)
# Harriet Novak
# 9.21.21

import math
from math import sqrt

# put function at the top and code at the bottom for clarity

def equationroots( a, b, c): 
        # calculating discriminant using formula
    dis = b * b - 4 * a * c # d = (b^2 - 4ac)
    sqrt_val = math.sqrt(abs(dis)) # square answer
      
    # checking condition for discriminant
    if dis > 0: 
        print(" real and different roots ") 
        r1 = ((-b + sqrt_val)/(2 * a)) # quadratic formula
        r2 = ((-b - sqrt_val)/(2 * a)) # quadratic formula
        roots = [r1, r2]  # creates an array, stores both roots
        return roots 
        
    elif dis == 0: 
        print(" real and same roots") 
        r1 = (-b / (2 * a)) # quadratic formula
        roots = [r1] # creates an array, only one root so only r1
        return roots
        
    else:
        print("Complex Roots") # discriminant is less than 0

calcreset = "yes" # if yes is typed re-enter values for a, b, and c

while calcreset != "x" : # if yes is typed
    a = int(input("Enter coefficient a: ")) # creates an input for a
    b = int(input("Enter coefficient b: ")) # creates an input for b
    c = int(input("Enter coefficient c: ")) # creates an input for c
   
  
    if a == 0: # If a is 0, then incorrect equation
        print("Input correct quadratic equation") # impossible to have 0x^2
  
    else:
        roots = equationroots (a, b, c) # the array storing the root values is equal to the function
        print(roots) # print out the roots

    calcreset = input("Input new set of values?") # asks question to trigger reset