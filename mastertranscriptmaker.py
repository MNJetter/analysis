import re
from sys import argv

script, filename = argv
subfile = open(filename,'r')
material = subfile.read()

quest = re.findall('[a-zA-Z]+', material)

# (for debugging the regex search)
print quest

# masterfile = open('MASTERTRANSCRIPT.txt','w')
# masterfile.write(quest)