degree = input("What degrees in F would you like to convert in Celsius? ")
n = (int(degree) - 32) / 1.8
print("That is roughly equivalent to " + "{:.1f}".format(n) + " degrees Celsius. ")
