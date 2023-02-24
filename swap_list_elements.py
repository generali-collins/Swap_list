# Collins Wanga

# Python program to swap first and last element of a list

def swapList(new_list):
	
	new_list[0], new_list[-1] = new_list[-1], new_list[0]

	return new_list
	

new_list = [1, 3, 5, 7, 9]
print(swapList(new_list))
