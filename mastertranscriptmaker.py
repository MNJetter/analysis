import re

subfile = open('3m-davidfrazee-int-e.srt','r')


#
#  Find a list of all strings that have a character
#
material = subfile.read()
quest = re.findall('[a-zA-Z]+', material)

#
#  Find a list of all lines that have a character
#
subfile.seek(0)                            # reset the file stream to the beginning
material_lines = subfile.readlines()       # read from the file as a list of lines
result_lines = []                          # this will be our list of resulting lines with characters
for line in material_lines:                # loop over all lines
    result = re.search('[a-zA-Z]+', line)  # regex result for the line
    if result != None :                    # if it contains something we will add this line to our list
        result_lines.append(line)          # add line to our list


#
#  Check our results by printing out to screen (for debugging)
#
for line in result_lines:
    print(line)


# (for debugging the regex search)
print(quest)

# masterfile = open('MASTERTRANSCRIPT.txt','w')
# masterfile.write(quest)