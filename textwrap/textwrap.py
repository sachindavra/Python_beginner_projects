"""This function will take a long string and an integer. It will break the string to number of characters defined by an interger"""

import textwrap3



def wrap_str():
	l = "This is a long string to test the functionality of the script. Let's check it out how it works."
	line_seperator = 4
	print(textwrap3.wrap(l,line_seperator))
	#wrapped = textwrap3.wrap(l,line_seperator)
	#for i in wrapped:
	#	print(i)
	

	print("\n-------------------\n")
	print(textwrap3.fill(l, line_seperator))

wrap_str()
