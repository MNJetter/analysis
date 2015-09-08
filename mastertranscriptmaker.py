import re

subfile = open('3m-davidfrazee-int-e.srt','r')
material = subfile.read()

quest = re.findall('[a-zA-Z]+', material)

# (for debugging the regex search)
print quest

# masterfile = open('MASTERTRANSCRIPT.txt','w')
# masterfile.write(quest)