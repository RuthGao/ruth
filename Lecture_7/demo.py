# Function

def print_a_string(a):
	print("###")
	print(a)
	print("###")
	return

# print_a_string("hello")

def add_num(a, b):
	c = a + b
	# print(c)
	return c

x = 3
y = 4
result = add_num(x, y)
result_2 = add_num(x, result)
# print(result_2)

def num_to_day(num):
	if num == 1:
		return "Monday"
	elif num == 2:
		return "Tuesday"
	elif num == 3:
		return "Wednesday"
	elif num == 4:
		return "Thursday"
	elif num == 5:
		return "Friday"
	elif num == 6:
		return "Saturday"
	elif num == 7:
		return "Sunday"
	else:
		return "Undefined"

day = num_to_day("7")
print(day)