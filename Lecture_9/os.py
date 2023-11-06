import os

fp = "animals.txt"

if os.path.exists(fp):
	os.remove(fp)
else:
	print('File doesn\'t exist.')
