import os

directories = os.listdir()
for directory in directories:
	if directory[2] == '.':
		os.rename(directory, '0' + directory)
for directory in directories:
	if directory[3] == '.':
		os.rename(directory, '0' + directory)