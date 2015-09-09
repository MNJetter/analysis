# get regex module and prepare the search function we're going to be using. The search function basically grabs any lowercase or capital letter.
import re
result = re.compile('[a-zA-Z]+')

######## old stuff from single file tests ########
## f = open('3m-davidfrazee-int-e.srt','r')     ##
## material = f.read()                          ##
## master = open('MASTERTRANSCRIPT.txt','w')    ##
## for subline in material.splitlines():        ##
##     if result.match(subline):                ##
##         master.write(subline + '\n')         ##
## f.close()                                    ##
## master.close()                               ##
##################################################

# TODO: make it work with a directory!
master = open('MASTERTRANSCRIPT.txt','w')
import os, glob
path = './'
for infile in glob.glob( os.path.join(path, '*.srt') ):
    f = open(infile,'r')
    material = f.read()
    for subline in material.splitlines():
    	if result.match(subline):
    		master.write(subline + '\n')
   	f.close()
master.close()