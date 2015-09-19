##################################################
## Begin CAT DEMO                               ##
##################################################
## The purpose of this demonstration is to      ##
## provide a quick proof-of-concept for the     ##
## idea of a computer-adaptive test that        ##
## uses the "2 strikes" method to navigate in a ##
## 6-level (base 3) definition of proficiency.  ##
##                                              ##
## The demonstration itself will not use real   ##
## English questions, but will use a set of     ##
## dummy questions, since it's the mechanic and ##
## not the content being showcased              ##
##################################################
## (c) 2015 SMATOOS, Inc.                       ##
##################################################

eng_level = 3
right_count = 0
wrong_count = 0
total_count = 0

answer_key = ['a','b','a','b','a','b','b','a','a','a','a','a','b','a','a','b','a','a','b','b']

while total_count < 20:
	if right_count == 2:
		eng_level += 1
		right_count = 0
		wrong_count = 0
		print "Moving to Level %d" % eng_level
	elif wrong_count == 2:
		eng_level -= 1
		right_count = 0
		wrong_count = 0
		print "Moving to Level %d" % eng_level
	else:
		student_answer = str(raw_input("Enter A or B: ")
		if student_answer == answer_key[total_count]
			right_count += 1
			total_count += 1
			print "Right!"
		elif student_answer != answer_key[total_count]
			wrong_count += 1
			total_count += 1
			print "Not quite."
print "Test complete! Your level is %s." % eng_level

##################################################
## End CAT DEMO                                 ##
##################################################
