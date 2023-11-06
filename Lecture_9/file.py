# Read from a file
# try:
# 	a = open("baby.txt", "r")

# 	a_arr = a.readlines()
# 	# print(a_arr)
# 	for i in a_arr:
# 		print(i, end="")

# 	a.close()
# except FileNotFoundError:
# 	print("File not found")
# except:
# 	print("Error caught")


# Write to a file
# try:
# 	b = open("write.txt", "a")

# 	b_arr = ["Hello worldddddddd\n", "This is the second line.......\n"]
# 	b.writelines(b_arr)

# 	b.close()
# except:
# 	print("Error caught")

# Seek()
try:
	c = open("animals.txt", "w+")

	print(c.readline(), end="")
	c.seek(-1, 2)
	print(c.readline(), end="")
	print(c.readline(), end="")

	c.close()
except:
	print("Error caught")
