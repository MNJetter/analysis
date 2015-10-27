# -*- coding: utf-8 -*-

import re

alpha = re.compile('[a-zA-Z]')

sentence1 = "This is an experimental sentence with 12 words and stuff in it."
sentence2 = "こんにちは"
sentences = [sentence1, sentence2]

def check_for_alpha(sentence):
	isalpha = False
	for letter in sentence:
		if alpha.match(letter):
			isalpha = True
	if isalpha:
		print "Yay!"
	else:
		print "Boo."

for sentence in sentences:
	check_for_alpha(sentence)