##################################################
## This script uses the natural language        ##
## toolkit to get a concordance, or list of     ##
## text around a specific word.                 ##
##################################################
## IMPORTANT!                                   ##
## Make sure that you are in the same directory ##
## as your target file to make this work!       ##
##                                              ##
## Please note that you will also need to have  ##
## NLTK v3 installed. Find installation         ##
## instructions at http://www.nltk.org/         ##
##################################################
## Written by A. Woolfrey                       ##
##################################################

# get the nltk tools
import nltk

# ask the user for a file name
fname = open(str(raw_input("File name: ")))

# turn the file into an NLTK tokenized object
t = fname.read();
tokens = nltk.word_tokenize(t)
text = nltk.Text(tokens)

# ask the user for a word
textword = str(raw_input("Word: "))

# get a concordance of the word
text.concordance(textword, lines=1000)