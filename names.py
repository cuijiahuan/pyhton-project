from name_function import get_formatted_name
print("Enter 'q' at any time to quit")
whil	e True:
	first = input("\nPlease give me a first name: ")
	if first == 'q':
		break
	last = input("Please give me a last name: ")
	if last == 'q':
		break
		
	formatted_name = get_formatted_name(first, last)
	print("\tNearly formatted name: " + formatted_name + '.')