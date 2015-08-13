# I want to be able to call capitalize_nested from main w/ various lists 
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

##############################################################################

# Body

def capitalize(word):
	if word[0].isupper() == False:
		word = word[0].title() + word[1:]
	return word

'''
def capitalize_nested(list_):


	new_list = []

	for i in list_:
		if isinstance(i, list):
			capitalize_nested(i)
		else:
			new_list.append(capitalize(i))

	print new_list
'''

# good formatting... mye?
def capitalize_nested(list_):
	l_new = [capitalize_nested(i)
		if (isinstance(i,list))
		else capitalize(i)
		for i in list_]

	return l_new

#t = ["hELLO","okaY", ["BOOM","meow"]]
#print(capitalize_nested(t))



##############################################################################
def main():
    pass

if __name__ == '__main__':
    main()