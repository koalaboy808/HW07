# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def nested_sum(list_):
	
	summed = 0

	for i in list_:
		if isinstance(i, list):
			nested_sum(i)
		else:
			summed += i
			#print("i is: " + str(i))
			#print("summed is: " + str(summed))
	return summed

'''
Hey Daniel! can you do this without using the sum function?
sum automatically knows how to sum appropriately... but I 
wouldn't know how to do the problem this way if the function didn't exist

def list_seperated(list_):
	l_new = [list_seperated(i) if (isinstance(i,list)) else i for i in list_]
	#return sum(l_new)
	print(l_new)

'''


##############################################################################
def main():
    pass

if __name__ == '__main__':
    main()
