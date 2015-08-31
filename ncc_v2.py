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

# get necessary modules
import nltk
from sys import argv

# get the file name and target word from user input with the script command
script, fname, textword = argv

# turn the file into an NLTK tokenized object
file = open(fname)
t = file.read();
tokens = nltk.word_tokenize(t)
text = nltk.Text(tokens)

# get a concordance of the word
text.concordance(textword, lines=1000)