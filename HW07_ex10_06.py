# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()
a = ["hello","HELLO"]

def is_sorted(list_):
	if list_ == sorted(list_):
		return True
	return False

##############################################################################
def main():
    pass

if __name__ == '__main__':
    main()