# Python Program 03 - Strings and Loops (ENGR4)
# Harriet Novak
# 2.23.21
# repo: https://github.com/hnovak94/Engineering4Notebook


txt = input("Type in your text, then press 'Enter'") # takes input, enter sentence
words = txt.split() # splits sentence into individual words
for w in words: # for each word in the 'words'array
    for letters in w: # break word into individual letters
        print (letters) # print individual letters
    print("-") # print "-" after word
    # loops again for next word