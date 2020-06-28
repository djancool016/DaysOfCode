from DataInput import *
sampleInput = [x.replace("\n","") for x in inputMethod("Input/Day01_DataType.txt")]

# input variable
i = 4
d = 4.0
s = 'HackerRank '

# Declare second integer, double, and String variables.
i2 = None
d2 = None
s2 = None

# Read and save an integer, double, and String to your variables.
# 'or' for default input

i2 = int(sampleInput[0])
d2 = float(sampleInput[1])
s2 = str(sampleInput[2])

# Print the sum of both integer variables on a new line.
print(i + i2)

# Print the sum of the double variables on a new line.
print(d + d2)

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s + s2)


# output :
# 16
# 8.0
# HackerRank is the best place to learn and practice coding!