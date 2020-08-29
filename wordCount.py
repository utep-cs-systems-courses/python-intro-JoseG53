#Assignment 1: WordCount  
#Author: Jose Gallardo
#Task: Count how many times a word appears in a file and write IN ALPHABETICAL ORDER the word and count e.g: Hello 3
#Will take in arguments (name of file to be read) and (name of file to be written to)

import sys, re

#Variable Declaration
CountedWords = {} #Dictionary for words
ftoread = sys.argv[1] #File to be read
ftowrite = sys.argv[2] #File to be written to


with open(ftoread, 'r') as f:
    for line in f:
        line = line.lower().strip() #lowercase and removes whitespace
        line = line.replace('-', " ") #removes - and sperates the words
        line = line.replace("'", " ") #removes the ' and sparates the two
        word = re.sub(r'[^\w\s]', '', line).split() #removes the rest of the puctutation and splits the str into a list of words
        for i in word:
            if (CountedWords.get(i) is None):
                CountedWords[i] = 1
            else:
                CountedWords[i] += 1

sortedWords = sorted(CountedWords)

with open(ftowrite, 'w') as f:
    for i in sortedWords:
        f.write(i + " " + str(CountedWords[i]) + "\n")


                
#print(CountedWords)
