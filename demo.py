filename = "name.txt"

with open(filename, 'w') as file_object:
	
	num = 1;
	while num < 5:
		name = input("Enter your name: ")
		file_object.write(str(num) + " : " + name + " enter this \n")
		print("Welcome to here, " + name)
		num += 1
		
