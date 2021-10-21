# Engineering IV Notebook
## Table of Contents
### Code
#### [Hello Python](https://github.com/hnovak94/Engineering4Notebook#-hello-python)
#### [Python Program 01](https://github.com/hnovak94/Engineering4Notebook#-python-program-01)
#### [Python Program 02](https://github.com/hnovak94/Engineering4Notebook#-python-program-02)
#### [Python Program 03](https://github.com/hnovak94/Engineering4Notebook#-python-program-03)
#### [Python Challenge - MSP](https://github.com/hnovak94/Engineering4Notebook#-python-challenge---msp)
### CAD
#### [Swing Arm](https://github.com/hnovak94/Engineering4Notebook#cad-test-part-1---swing-arm)
#### [Skateboard](https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/skateboard.PNG)

## Code

### ○ Hello Python

[Code](https://github.com/hnovak94/Engineering4Notebook/blob/main/diceroller%20(1).py)

[Spicy Code](https://github.com/hnovak94/Engineering4Notebook/blob/main/spicydr.py)
  
#### Assignment Description

This assignment we shifted away from working in Beagleterm, and began using and online [python IDE](https://www.online-python.com/) to code. The task was to code an automatic dice roller that would produce a random number between 1 and 6. 

The spicier version of this assignment offers the user the option to choose the number of sides and the number of die rolled. 

#### Working Code

<img src="https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/drcapture.PNG" height=200>

#### Reflection

For this assignment we had to start using functions again, and it was a return to coding after months away. 

The spicier version was done by creating more inputs (for number of sides and number of dice) and the use of nested if loops. 



### ○ Python Program 01

[Code](https://github.com/hnovak94/Engineering4Notebook/blob/main/calculator.py) 

#### Assignment Description

The task for this assignment was to create a calculator on python where you could enter two values and the function doMath would give you the sum, the difference, the product, the quotient, and the modulo. The modulo is the remainder of a division problem, division without decimals.

#### Working Code

<img src="https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/calcoutput.PNG" height=200>

#### Reflection

The modulo is found using "%". [This article](https://www.programiz.com/python-programming/examples/calculator) was very helpful in getting started. An issue with this assignment was the cannot concatenate error. [This article](https://careerkarma.com/blog/python-typeerror-can-only-concatenate-str-not-int-to-str/) was very helpful with this issue. I had to convert the returns at the end to strings using str().

### ○ Python Program 02

[Code](https://github.com/hnovak94/Engineering4Notebook/blob/main/Code/quadcalc.py)

#### Assignment Description

For this assignment we had to create a program that would find the roots of a quadratic when given inputs for a, b, and c. 

#### Working Code

<img src="https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/qcalc.capt.PNG" height=200>

#### Reflection

<img src="https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/dis.capt.PNG" height=150>

The first step for this assignment was to figure out the discriminant. The above picture shows how that value is found. This was a helpful [code](https://www.geeksforgeeks.org/python-program-to-solve-quadratic-equation/) starter which shows how to use the quadratic formula in python. 
[This](https://www.codegrepper.com/code-examples/python/how+to+return+an+array+in+python) was helpful in understanding an array. One thing I learned is that it's very helpful to put the actual code you are running below the function. It made it much easier to reset the code so the user could re-enter new values for for a, b, and c. 

### ○ Python Program 03

[Code](https://github.com/hnovak94/Engineering4Notebook/blob/main/Code/strloop.py)

#### Assignment Description

For this assignment we had to write a program that asked the user to enter a simple sentence. The code would then split the individual words into letters, printing each letter on a different line, with a hyphen after each word. 

#### Working Code

<img src="https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/strings.capt.PNG" height=200>

#### Reflection

For this assignment we had to use the split() function to divide a simple sentence into an array of individual words. [This article](https://www.w3schools.com/python/ref_string_split.asp) was helpful in understanding a split. Then we had to use a series of for loops to split the individual words into their most basic parts. This was done through a series of variables and arrays. The code is commented to show how the for loops work. 

### ○ Python Challenge - MSP

[Code](https://github.com/hnovak94/Engineering4Notebook/blob/main/Code/hangman-msp.py)

#### Assignment Description
For this assignment we had to create a program that would play a game of hangman. Player 1 would enter a word, and it would then disappear. Player 2 would enter a guess and the hangman frame would appear. With every entered guess the program would tell the player whether the answer was in the word or not. If it is, then a body part is added to the frame, if it's correct, it will be stored in correct guesses. 

#### Working Code
<img src="https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/hangmancapt.PNG" height=200>

#### Reflection
This assignment we had to use multiple functions. There was a function to replace the blanks with letters, and a function to slowly add to the frame as the number of incorrect guesses increases. The hardest part of this code was replacing the blanks. The commenting of my code will explain how that was done. 

## CAD

### CAD Test Part #1 - Swing Arm

#### Assignment Description
For this assignment we had to design a swing arm based on a design drawing. 

#### Final Product
<img src="https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/sa.sketch.PNG" height=200>

##### Configuration 1 
<img src="https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/sa.capt.PNG" height=150>
Configuration 2

#### Reflection

The hardest part of this assignment was to figure out dimensions from the sketch that weren't explicitly given. Also, one thing that was very important was deciding the order of the steps. I ended up having to do extra steps later because I didn't plan from the beginning. 

### Intro to CAD

[Onshape Document](https://cvilleschools.onshape.com/documents/d45b23f7c4ae5c0bb560e92e/w/1cb96744ab6dc27835275258/e/fe2f0be7eebf92a04bee64b3)

#### Assignment Description
For this assignment we had to follow steps as an intro to CAD that shows you how to make a skateboard on Onshape. 

#### Final Product
<img src="https://github.com/hnovak94/Engineering4Notebook/blob/main/Media/skateboard.PNG" height="200">

#### Reflection

The instructions were pretty explicit, so the main issue was just motivation. However, there were some issues with mating in the assembly. 
