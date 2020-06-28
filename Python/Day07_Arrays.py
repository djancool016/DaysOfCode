from DataInput import *
sampleInput = [x.replace("\n","") for x in inputMethod("Input/Day07_Arrays.txt")]

# map() can listify the list of strings individually
array = list(map(int, sampleInput[1].rstrip().split()))
array.reverse()
for num in array:
    print(str(num) + " ", end="")

# Sample Input :
# 4
# 1 4 3 2

# Sample Output :
# 2 3 4 1