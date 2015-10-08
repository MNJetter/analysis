##################################################
## Begin STRIPPER script.                       ##
##################################################
## This is a script to take all of the          ##
## English-language SRT files in a directory,   ##
## strip them of their timestamps, and re-save  ##
## them as TXT files for the purpose of         ##
## language analysis.                           ##
##################################################
## (c) 2015 SMATOOS, Inc.                       ##
##################################################

# import Regex and set up the basic search criteria to find English lines
import re
english = re.compile('[a-zA-Z]')

# define the SRT to be read from
filename = 's136-in-the-office---greeting'

# open up the SRT to be read from
oldfile = open(filename + '.srt','r')
oldfile_content = oldfile.read()

# make a TXT file to write the transcript to
newfile = open(filename + '---transcript.txt','w')

# write the transript lines
for line in oldfile_content.splitlines():
	if english.match(line):
		newfile.write(line + '\n')

# close out the files
newfile.close()
oldfile.close()

##################################################
## End STRIPPER script.                         ##
##################################################
