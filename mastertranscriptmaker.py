import re

subfile = open('3m-davidfrazee-int-e.srt','r')
material = subfile.read()

quest = re.compile('[a-zA-Z]+')
masterfile = open('MASTERTRANSCRIPT.txt','w')

for subline in material.splitlines():
	if quest.match(subline):
		masterfile.write(subline + '\n')