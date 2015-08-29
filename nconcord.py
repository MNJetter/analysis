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
## NLTK 3 installed. Find installation          ##
## instructions at http://www.nltk.org/         ##
##################################################
## Written by A. Woolfrey                       ##
##################################################

# get the nltk tools
import nltk

# ask the user for a file name 
print """

WARNING
Make sure that you are in the same directory 
as your target file to make this work!
When you enter your file:
- include the file suffix.
- put the file name in single quotes
Example: 'room.txt'

---------------
"""
file = open(str(input("File name: ")))

# turn the file into an NLTK tokenized object
t = file.read();
tokens = nltk.word_tokenize(t)
text = nltk.Text(tokens)

# ask the user for a word
print """
Which word would you like to explore?
(Don't forget the single quotes!)
"""
textword = str(input("Word: "))

# get a concordance of the word
print """

---------------

"""
text.concordance(textword, lines=1000)