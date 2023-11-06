a = 1

try:
	if a < 2:
		raise TypeError()
except ValueError:
	print("ValueError caught")
except:
	print("Error caught")