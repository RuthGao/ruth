print("Option A")
n = input('Quantity: ')
n = int(n)
m = input("Price: ")
m = float(m)
per_unit_A = m / n
print("")

print("Option B")
x = input('Quantity: ')
x = int(x)
y = input("Price: ")
y = float(y)
per_unit_B = y / x
print("")

if per_unit_A > per_unit_B:
    print("Option B is cheaper!")
elif per_unit_A < per_unit_B:
    print("Option A is cheaper!")
else:
    print('They\'re the same!')



