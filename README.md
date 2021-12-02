# Engineering IV Notebook
## Table of Contents
### Code
#### [Hello Python - Dice Roller](https://github.com/hnovak94/Engineering4Notebook#-hello-python)
#### [Python Program 01 - Calculator](https://github.com/hnovak94/Engineering4Notebook#-python-program-01)
#### [Python Program 02 - Quadratic Calculator](https://github.com/hnovak94/Engineering4Notebook#-python-program-02)
#### [Python Program 03 - Strings and Loops](https://github.com/hnovak94/Engineering4Notebook#-python-program-03)
#### [Python Challenge - MSP](https://github.com/hnovak94/Engineering4Notebook#-python-challenge---msp)
#### [RPi GPIO Pin Introduction](https://github.com/hnovak94/Engineering4Notebook/blob/main/README.md#rpi-gpio-pin-introduction)
#### [RPi Safe Shutdown Button](https://github.com/hnovak94/Engineering4Notebook#rpi-safe-shutdown-button)
#### [GPIO Pins - I2C](https://github.com/hnovak94/Engineering4Notebook#gpio-pins---i2c-1)
### CAD
#### [CAD Test Part #1 - Swing Arm](https://github.com/hnovak94/Engineering4Notebook#cad-test-part-1---swing-arm)
#### [Intro to CAD 2.1-2.4 - Skateboard](https://github.com/hnovak94/Engineering4Notebook#intro-to-cad-21-24)
#### [Intro to CAD 3.1-3.4 - Lego](https://github.com/hnovak94/Engineering4Notebook#intro-to-cad-31-34)
#### [Multi-tool](https://github.com/hnovak94/Engineering4Notebook/blob/main/README.md#multi-tool-1)


## Code

### Hello Python

[Code](https://github.com/hnovak94/Engineering4Notebook/blob/main/diceroller%20(1).py), [Spicy Code](https://github.com/hnovak94/Engineering4Notebook/blob/main/spicydr.py)
  
#### Assignment Description

This assignment we shifted away from working in Beagleterm, and began using and online [python IDE](https://www.online-python.com/) to code. The task was to code an automatic dice roller that would produce a random number between 1 and 6. 

The spicier version of this assignment offers the user the option to choose the number of sides and the number of die rolled. 

#### Working Code

<img src="https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/drcapture.PNG" height=200>

#### Reflection

For this assignment we had to start using functions again, and it was a return to coding after months away. 

The spicier version was done by creating more inputs (for number of sides and number of dice) and the use of nested if loops. 



### Python Program 01

[Code](https://github.com/hnovak94/Engineering4Notebook/blob/main/calculator.py) 

#### Assignment Description

The task for this assignment was to create a calculator on python where you could enter two values and the function doMath would give you the sum, the difference, the product, the quotient, and the modulo. The modulo is the remainder of a division problem, division without decimals.

#### Working Code

<img src="https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/calcoutput.PNG" height=200>

#### Reflection

The modulo is found using "%". [This article](https://www.programiz.com/python-programming/examples/calculator) was very helpful in getting started. An issue with this assignment was the cannot concatenate error. [This article](https://careerkarma.com/blog/python-typeerror-can-only-concatenate-str-not-int-to-str/) was very helpful with this issue. I had to convert the returns at the end to strings using str().



### Python Program 02

[Code](https://github.com/hnovak94/Engineering4Notebook/blob/main/Code/quadcalc.py)

#### Assignment Description

For this assignment we had to create a program that would find the roots of a quadratic when given inputs for a, b, and c. 

#### Working Code

<img src="https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/qcalc.capt.PNG" height=200>

#### Reflection

<img src="https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/dis.capt.PNG" height=150>

The first step for this assignment was to figure out the discriminant. The above picture shows how that value is found. This was a helpful [code](https://www.geeksforgeeks.org/python-program-to-solve-quadratic-equation/) starter which shows how to use the quadratic formula in python. 
[This](https://www.codegrepper.com/code-examples/python/how+to+return+an+array+in+python) was helpful in understanding an array. One thing I learned is that it's very helpful to put the actual code you are running below the function. It made it much easier to reset the code so the user could re-enter new values for for a, b, and c. 



### Python Program 03

[Code](https://github.com/hnovak94/Engineering4Notebook/blob/main/Code/strloop.py)

#### Assignment Description

For this assignment we had to write a program that asked the user to enter a simple sentence. The code would then split the individual words into letters, printing each letter on a different line, with a hyphen after each word. 

#### Working Code

<img src="https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/strings.capt.PNG" height=200>

#### Reflection

For this assignment we had to use the split() function to divide a simple sentence into an array of individual words. [This article](https://www.w3schools.com/python/ref_string_split.asp) was helpful in understanding a split. Then we had to use a series of for loops to split the individual words into their most basic parts. This was done through a series of variables and arrays. The code is commented to show how the for loops work. 



### Python Challenge - MSP

[Code](https://github.com/hnovak94/Engineering4Notebook/blob/main/Code/hangman-msp.py)

#### Assignment Description
For this assignment we had to create a program that would play a game of hangman. Player 1 would enter a word, and it would then disappear. Player 2 would enter a guess and the hangman frame would appear. With every entered guess the program would tell the player whether the answer was in the word or not. If it is, then a body part is added to the frame, if it's correct, it will be stored in correct guesses. 

#### Working Code
<img src="https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/hangmancapt.PNG" height=200>

#### Reflection
This assignment we had to use multiple functions. There was a function to replace the blanks with letters, and a function to slowly add to the frame as the number of incorrect guesses increases. The hardest part of this code was replacing the blanks. The commenting of my code will explain how that was done. 

### RPi GPIO Pin Introduction

[Code](https://github.com/hnovak94/Engineering4Notebook/blob/main/Python/ledblink.py)

#### Assignment Description

For this assignment we had to get the raspberry pi working in BeagleTerm, and to make the raspberry pi alternate two blinking LEDs. 

#### Reflection

The difficult part of this assignment was the GPIO pins, because the code in itself was very simple. Another factor in this assignment was navigating Beageterm, but I'm not having issues because I already feel comfortable with Terminal, which is very similar. Important commands to remember are ' python3 codename.py ' and ' nano codename.py ' to edit the code. Another important thing to remember is to not change the wiring while the pi is plugged in. The command to shutdown the pi is ' sudo shutdown -h now '. 

### RPi Safe Shutdown Button

[Code](https://github.com/hnovak94/Engineering4Notebook/blob/main/Python/shutdownpi.py) - See below for code credit

#### Assignment Description

The object of this assignment was to add a button that would safely shutdown and/or reboot the raspberry pi, without needing typed input into BeagleTerm. [This](https://learn.sparkfun.com/tutorials/raspberry-pi-safe-reboot-and-shutdown-button/all) was the tutorial and code used to add the button. 

#### Reflection

This assignment was mostly trial and error, because I kept making small mistakes. This assignment was good practice for quickly manoeuvring in the terminal, and how to modify and work with code that is not written by me. 

### GPIO Pins - I2C

[Code](https://github.com/hnovak94/Engineering4Notebook/blob/main/Code/gpiopins.py), [Wiring Diagram](https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/pinswd.png)

#### Assignment Description

The goal of this assignment was to connect an accelerometer and an LCD screen so that the screen would print the values from the accelerometer. 

#### Working Code

<img src="https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/pinsproof.png" height="250"> <img src="https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/pinswd.png" height="250">

#### Reflection

This assignment didn't include very much original code, but involved a combination of two codes from the accelerometer [library](https://github.com/hnovak94/Engineering4Notebook/tree/main/Adafruit_Python_LSM303) and the LCD [library](https://github.com/hnovak94/Engineering4Notebook/tree/main/Adafruit_Python_SSD1306). The first was this [code](https://github.com/hnovak94/Engineering4Notebook/blob/main/Adafruit_Python_LSM303/examples/simpletest.py) which prints out the accelerometer values to the terminal window. The second [code](https://github.com/hnovak94/Engineering4Notebook/blob/main/Adafruit_Python_SSD1306/examples/shapes.py) prints out shapes on the LCD screen. The trickiest part about this assignment was figuring out what parts of the code to keep and which to delete, which required some trial and error. [This](https://raspberrypi.stackexchange.com/questions/61396/how-to-write-string-and-variables-on-lcd-with-lcd-string) was helpful for turning the variable into a string to be printed to the LCD screen.

## CAD

[Onshape Document](https://cvilleschools.onshape.com/documents/4938fa387c8e90e94338e4b1/w/9bf53b1e2e9fc5edd3a2e3a7/e/21c65779804e4c888af6c09e)

### CAD Test Part #1 - Swing Arm

#### Assignment Description
For this assignment we had to design a swing arm based on a design drawing. 

#### Final Product

##### Configurations 1 + 2
<img src="https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/sa.sketch.PNG" height=250><img src="https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/config2.PNG" height="300">

##### Table of Variables

<img src="https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/variables.PNG" height="250">

#### Reflection

The hardest part of this assignment was to figure out dimensions from the sketch that weren't explicitly given. Also, one thing that was very important was deciding the order of the steps. I ended up having to do extra steps later because I didn't plan from the beginning. The second configuration also messed up the extrusion, so edits had to be made. This was also my first time using variables for lengths and angles in CAD. 



### Intro to CAD 2.1-2.4

[Onshape Document](https://cvilleschools.onshape.com/documents/d45b23f7c4ae5c0bb560e92e/w/1cb96744ab6dc27835275258/e/fe2f0be7eebf92a04bee64b3)

#### Assignment Description
For this assignment we had to follow steps as an intro to CAD that shows you how to make a skateboard on Onshape. 

#### Final Product
<img src="https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/skateboard.PNG" height="200">

#### Reflection

The instructions were pretty explicit, so the main issue was just motivation. However, there were some issues with mating in the assembly. For the first part I learned more efficient ways to add holes. For the second part I learned how to create different parts in the same part folder basing them off of each other's geometry. For part three I got a reminder of how to use the revolve tool. For the last part, this part took me the longest, I learned how to more efficiently add screws and nuts into the assembly. 



### Intro to CAD 3.1-3.4

[Onshape Document](https://cvilleschools.onshape.com/documents/91cec67db0eb7e409734e77b/w/dfcd322a61304ceab53a4d4f/e/7d2524be0779493984d6a4b3)

### Assignment
We had to use configurations and variables to make different shapes, sizes, and colors of legos. [Here](https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/configtable.PNG) are the configuration tables for the different legos.

<img src="https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/configtable.PNG" height="400">

I used the different configurations and snap mates to create a duck out of legos. 

<img src="https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/duck.PNG" height="250"><img src="https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/duck2.PNG" height="250">

### Reflection

I had used configurations in Onshape prior to this assignment, but was not confident in my use of them. I'm not sure to what extent I will retain the skills from this assignment, but I now know different ways to make CAD design easier and more efficient, particularly if there is variation in different parts. Instead of having to make many different parts individually, with one part studio you can make dozens of parts. 

### Multi-tool

#### Assignment
The main point of this assignment was to learn how to use the laser cutter. The actual CAD design was relatively simple. 

<img src="https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/mtcapt.PNG" height="250"><img src="https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/mtdrawcapt.PNG" height="250">

The image on the right shows the drawing to be laser cut. The red lines represent what will be cut, and the blue lines show what will  be engraved on the acryllic. 

#### Reflection

Now I feel more comfortable laser cutting parts on my own. It is also easier now that we don't have to use Adobe Illustrator, we can just make the drawing to be laser cut in Onshape. 


