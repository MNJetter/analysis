##################################################
## Begin STRIPPER script.                       ##
##################################################
## This is a script to take all of the          ##
## English-language SRT files in a directory,   ##
## strip them of their timestamps, and re-save  ##
## them as TXT files for the purpose of         ##
## language analysis.                           ##
##################################################
## Written by Aly Sevre                         ##
## (c) 2015 SMATOOS, Inc.                       ##
##################################################

# import Regex and set up the basic search criteria to find English lines
import re
alpha = re.compile('[a-zA-Z]')

# TODO: Figure out some way for the user to input a target directory
# TODO: Figure out some way to do the script for each file in the target directory instead of manually hard-coding the file name here

##################################################
## Custom functions for language processing     ##
##
## Write transcript lines to text
def write_transcript_text_file(srt_full_content, txt_filename):
	newfile = open(txt_filename, 'w')              # open file
	for line in srt_full_content.splitlines():
		if alpha.match(line):                    # check line for English
			newfile.write(line + '\n')             # write line to file
	newfile.close()                                # close file
##
## Open, read, and close the file in a simple function
def read_file_contents(filename):
	myfile = open(filename, 'r')
	r = myfile.read()
	myfile.close()
	return r
##
def prepare_srt_filename(filename):
	# Check to see if the given filename has an 'srt' suffix
	# if not, add one
	srt_suffix = '.srt'  # suffix for srt file
	srt_suffix_length = len(srt_suffix)  # length of suffix

	if filename[-srt_suffix_length:] == srt_suffix:  # check if suffix is in given filename
		srtfilename = filename
		file_root = filename[:-srt_suffix_length]
	else:    # if it isn't there, do this
		srtfilename = filename + '.srt'
		file_root = filename

	return srtfilename, file_root
##
## End functions                                ##
##################################################

if __name__ == '__main__':
	# define the SRT to be read from
	filename = 's136-in-the-office---greeting'

	# TODO: future function to create, so we can read a list of files
	#potential_files = get_files_from_directory(some_dir)
	# practice list until above function is written
	potential_files = ['file1.srt', 'file2.srt']

	for file in potential_files:
		if file[-4:] == '.srt':
			# get srt_name, and root name
			srt_name, root_name = prepare_srt_filename(filename)
			old_file_content = read_file_contents(srtfilename)

			# make a TXT file to write the transcript to
			transcript_suffix = '---transcript.txt'
			txt_filename = root_name + transcript_suffix

			write_transcript_text_file(old_file_content, txt_filename)


##################################################
## End STRIPPER script.                         ##
##################################################
