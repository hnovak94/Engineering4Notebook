# Python Challenge - MSP (ENGR4)
# Harriet Novak
# 9.28.21
# repo: https://github.com/hnovak94/Engineering4Notebook

def hangman(miss): # deletes hangman as miss increases 
    if miss == 0:
        print("  ---  \n"
              "    |  \n")
        
    if miss == 1:
        print("  ---  \n"
              "    |  \n"
              "    0  \n")
    
    if miss == 2:
        print("  ---  \n"
              "    |  \n"
              "    0  \n"
              "   /   \n")
       
    if miss == 3:
        print("  ---  \n"
              "    |  \n"
              "    0  \n"
              "   /|  \n")
        
    if miss == 4:
        print("  ---  \n"
              "    |  \n"
              "    0  \n"
              "   /|\\\n")
    if miss == 5:
         print("  ---  \n"
              "    |  \n"
              "    0  \n"
              "   /|\\\n"
              "    |  \n")
    if miss == 6:
        print("  ---  \n"
              "    |  \n"
              "    0  \n"
              "   /|\\\n"
              "    |  \n"
              "   /   \n")
    if miss == 7:
        print("  ---  \n"
              "    |  \n"
              "    0  \n"
              "   /|\\\n"
              "    |  \n"
              "   / \\\n")
def check(guess, word):
    
    answer = list(prevguess)  # Convert existing word to a list of characters
    
    for position, character in enumerate(word):
        if character == guess:  # we found a match
            answer[position] = guess
            
    joined_answer = ''.join(answer)  
        
guessAgain = "yes"   # used to enable continuous guesses

miss = 0 # number of missed guesses begins at 0
word = input(str("Player 1, enter word:")) # input for initial word
print("\n" * 50) # clears screen by adding 50 blank lines

hangman(miss) # prints hangman
blanks = "-" * len(word) # prints dashes for letters in word

while guessAgain != "x": # keep guessing
    guess = input("Player 2, enter guess:") # input for entered guess
    if guess in word: # checks word for the guess entered, if correct...
        print("correct!") # print correct
        correct = [guess] # store guess in correct guesses
    else: # if incorrect...
        print("letter not in word") # print letter not in word
        miss = miss + 1 # add one number to guesses
        wrong = [guess] # store guess in wrong guesses
    if miss >= 7: # if there are more than 7 wrong answers, the hangman is empty
        guessAgain = "x" # then exit out of loop
        print("you lost") # print you lost
        
    hangman(miss) # calls function to print hangman according to miss number