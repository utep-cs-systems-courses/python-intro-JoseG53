#Assignment 1: WordCount  
#Author: Jose Gallardo
#Task: Count how many times a word appears in a file and write IN ALPHABETICAL ORDER the word and count e.g: Hello 3
#Will take in arguments (name of file to be read) and (name of file to be written to)

import sys

#Variable Declaration
CountedWords = {} #Dictionary for words
ftoread = sys.argv[1] #File to be read
ftowrite = sys.argv[2] #File to be written to


with open(ftoread, 'r') as f:
    for line in f:
        words =  line.split()
        for i in words:
            i = i.replace('.', '') #used to strip punctuation from words
            i = i.replace(',', '')
            i = i.replace(':', '')
            i = i.replace(';', '')
            i = i.replace('"', '')
            if (CountedWords.get(i) is None):
                CountedWords[i] = 1 #adds word to dictionary
            elif (CountedWords.get(i)):
                CountedWords[i] +=1 #updates word count

sortedWords = sorted(CountedWords)

with open(ftowrite, 'w') as f:
    for i in sortedWords:
        f.write(i + " " + str(CountedWords[i]) + "\n")


                
#print(CountedWords)
