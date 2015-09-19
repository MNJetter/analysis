##################################################
## TRANSCRIPTER                                 ##
##################################################
## This script, working from ~/analysis/, takes ##
## all the SRT files from ~/interview_srts/ and ##
## makes a single text file of the EN lines.    ##
##################################################
## (c) 2015 Aly Woolfrey                        ##
## Licensed for unlimited use, modification, or ##
## distribution in perpetuity to SMATOOS, Inc.  ##
##################################################

import re
import os, glob

# regex function that asks for any capital or lowercase letters
result = re.compile('[a-zA-Z]+')

# tells the computer where to look for SRT files (target directory)
path = '../interview_srts/'

# makes an empty master transcript file in the target directory
master = open(path + 'MASTERTRANSCRIPT.txt','w')

# reads all SRTs in the target directory
for stuff in glob.glob(os.path.join(path, '*.srt')):
    f = open(stuff,'r')
    material = f.read()
# finds EN lines with the regex function and writes them to the master file
    for subline in material.splitlines():
    	if result.match(subline):
    		master.write(subline + '\n')
   	f.close()
master.close()

##################################################
## End TRANSCRIPTER                             ##
##################################################