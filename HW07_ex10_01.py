# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def nested_sum(list_):
	l_new = [nested_sum(i) if (isinstance(i,list)) else i for i in list_]
	return sum(l_new)
	#print(l_new)




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
	list_1 = [1, [2], 2, 3, [1, 3, 6]]
	list_2 = [[[[2]], 3, 1, 1, [1,1,1,1,1]], 1]
	list_3 = []
	list_4 = [1]
	print nested_sum(list_1)  # 18
	print nested_sum(list_2)  # 13
	print nested_sum(list_3)  # 0
	print nested_sum(list_4)  # 1

if __name__ == '__main__':
    main()
