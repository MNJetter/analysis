# get regex module and prepare the search function we're going to be using. The search function basically grabs any lowercase or capital letter.
import re
quest = re.compile('[a-zA-Z]+')

# call up the file(s) to be read
# TODO: Change '3m-davidfrazee-it-e.srt' to some sort of thing that can grab all the files in the current directory instead.
subfile = open('3m-davidfrazee-int-e.srt','r')
material = subfile.read()

# make a file to write the lines to
masterfile = open('MASTERTRANSCRIPT.txt','w')

# split the SRT files into lines and write all the ones that contain a match to the regex function into the transcript file.
for subline in material.splitlines():
	if quest.match(subline):
		masterfile.write(subline + '\n')

# closing files is a good idea after they've been opened...
subfile.close()
materfile.close()