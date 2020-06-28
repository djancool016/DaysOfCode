from DataInput import *
sampleInput = [x.replace("\n","") for x in inputMethod("Input/Day05_Loops.txt")]

for i in range(len(sampleInput)):
    n = int(sampleInput[i])
    for j in range (1,11):
        k = n*j
        print(f"{n} x {j} = {k}")

# output :
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 2 x 10 = 20