x = 3 # Here, the variable x is a global variable

def add(a, b):
	c = a + b # Here, a, b, and c are all local variables
	print(x)
	return c

# print(x)

num_1 = 3
num_2 = 4
s = add(num_1, num_2)
print(s)