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

        
guessAgain = "yes"   # used to enable continuous guesses
correct = "" # establishes correct as variable
wrong = "" # establishes wrong as variable 
miss = 0 # number of missed guesses begins at 0
word = input(str("Player 1, enter word:")) # input for initial word
print("\n" * 50) # clears screen by adding 50 blank lines

hangman(miss) # prints hangman
blanks = "-" * len(word) # creates dashes for letters in word (length of word)
print(blanks) # prints blanks

def check(word, correct, blanks): # replaces blanks with letters
    for i in range(len(word)): # position of letter as a number in range of number of letters
        if word[i] in correct: # guess is in word...
            blanks = blanks[:i] + word[i] + blanks[i + 1:] 
            # first, go to position of letter and replace only that letter. 
            # then move to next position
    print(blanks) # prints out blanks
            
while guessAgain != "x": # keep guessing
    guess = input("Player 2, enter guess:") # input for entered guess
    if guess in word: # checks word for the guess entered, if correct...
        print("correct!") # print correct
        correct = correct + guess # store guess in correct guesses
    else: # if incorrect...
        print("letter not in word") # print letter not in word
        miss = miss + 1 # add one number to guesses
        wrong = wrong + guess # store guess in wrong guesses
        print(wrong) # print missed guesses
    if miss >= 7: # if there are more than 7 wrong answers, the hangman is empty
        guessAgain = "x" # then exit out of loop
        print("you lost :(") # print you lost
        
    hangman(miss) # calls function to print hangman according to miss number
    check(word, correct, blanks) # calls function to replace blanks with correct guesses