#The code below demonstrates how to create a new file or overwrite an existing one:

filename = "newfile.txt"

# Open the file with write permissions
myfile = open(filename, 'w')

# Add content to the file
myfile.write('Written with Python\n')

# Ensure the file is closed post operations
myfile.close()


#If you wish to retain the existing content and merely add more to a file, the ‘a’ parameter is your go-to:

# The 'a' flag instructs Python to preserve the file contents and add new content at the end.
myfile = open(filename, 'a')

# Add your desired line
myfile.write('Appended with Python\n')

# Always close the file after operations
myfile.close()