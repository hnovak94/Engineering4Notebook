
# Python Program 01 - Calculator (ENGR4)
# Code bn2 Harriet Novak
# 9.15.21
# repo: https://github.com/hnovak94/Engineering4Notebook
import math # python math library
  
n1 = int(input("Enter first number: ")) # creates an input for the first number
n2 = int(input("Enter second number: ")) # creates an input for the second number

def doMath(n1, n2, z): # doMath function n1: first input, n2: second input, z: math function being called
    if z == 1: # if z is option 1 (see bottom)
        return n1 + n2 # do addition
    if z == 2: # if z is option 2
        return n1 - n2 # do subtraction
    if z == 3: # if z is option 3 
        return n1 * n2 # do multiplication
    if z == 4: # if z is option 4
        return n1 / n2 # do division
    if z == 5: # if z is option 5 
        return n1 % n2 # find Modulo
        # modulo is the remainder, e.g. 3/2 remainder of 1. modulo = 1
    
print("Sum:\t\t" + str(doMath(n1,n2,1))) # prints addition answer
print("Difference:\t" + str(doMath(n1,n2,2))) # prints subtraction answer
print("Product:\t" + str(doMath(n1,n2,3))) # prints multiplication answer
print("Quotient:\t" + str(doMath(n1,n2,4))) # prints division answer
print("Modulo:\t\t" + str(doMath(n1,n2,5))) # prints modulo (remainder)