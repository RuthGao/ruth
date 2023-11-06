a = 3
b = a # copy the value from a and paste it into b
a = 2
# print(b)

arr_1 = [1, 2, 3]
arr_2 = arr_1 # arr_2 will be pointed to the same array arr_1 is pointing to.
arr_1[1] = 3
print(arr_2)
