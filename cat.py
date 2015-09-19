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


#
#  we can use this object to do the counting for us
#
class Count:
    right_count = 0
    wrong_count = 0
    total_count = 0
    current_level = 3

    #
    #  __init__  : this is done when the object is first created
    #
    def __init__(self):
        self.right_count = 0
        self.wrong_count = 0
        self.total_count = 0
        self.current_level = 3

    #  reset the right & wrong counts
    def reset(self):
        self.right_count = 0
        self.wrong_count = 0

    #  Check if we need to change level and update
    def update(self):
        if self.right_count == 2:
            self.current_level += 1  # TODO make sure current level doesn't exceed a level maximum
            self.reset()
            print("Moving to Level %d" % self.current_level)

        elif self.wrong_count == 2:
            self.current_level -= 1  # TODO make sure current level is positive (or non-negative)
            self.reset()
            print("Moving to Level %d" % self.current_level)

    def was_right(self):
        self.right_count += 1
        self.total_count += 1
        self.update()

    def was_wrong(self):
        self.wrong_count -= 1
        self.total_count += 1
        self.reset()



answer_key = ['a', 'b', 'a', 'b', 'a', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'b', 'a', 'a', 'b', 'a', 'a', 'b', 'b']

#
#  We will ask 20 questions, and for each question we will change levels if necessary
#  by necessary we mean if right_count or wrong_count == 2
#

#
#  create a counter to do our counting for us
#
counter = Count()

while counter.total_count < 20:
    qu_number = counter.total_count
    student_answer = str(raw_input("Enter A or B: ")).lower() # change to lowercase THEN check the answer
    if student_answer == answer_key[qu_number]:
        counter.was_right()
        print("Right!")
    else:  # this can be an else, since we know it isn't right, it must be wrong
        counter.was_wrong()
        print("Not quite.")
print("Test complete! Your level is %s." % eng_level)

##################################################
## End CAT DEMO                                 ##
##################################################
