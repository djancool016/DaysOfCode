from DataInput import *
sampleInput = [x.replace("\n","") for x in inputMethod("Input/Day06_Lets_Riview.txt")]

N = int(sampleInput[0])

for x in range(1,N+1):

    for y in range(0, len(sampleInput[x])):
        if y % 2 == 0:
            print(sampleInput[x][y], end='')

    print (" ", end="")

    for y in range(0, len(sampleInput[x])):
        if y % 2 != 0:
            print(sampleInput[x][y], end='')

    print ("")