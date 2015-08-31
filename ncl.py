##################################################
## This script uses the natural language        ##
## toolkit to get collocations, or list of      ##
## words that appear frequently together.       ##
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
import re
from sys import argv

# get the file name and target word from user input with the script command
script, fname = argv

# turn the file into an NLTK tokenized object
file = open(fname)
t = file.read();
tokens = nltk.word_tokenize(t)
text = nltk.Text(tokens)

# get collocations for the text
text.collocations()