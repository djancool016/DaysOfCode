from Input.DataInput import *
sampleInput = inputMethod("Input/Day03_Conditional_Statements.txt")

for x in range(len(sampleInput)):

    N = float(sampleInput[x])

    if (N>20 and N%2==0):
        print (f"{N} is even number > 20")
    elif (6<=N<=20 and N%2==0):
        print (f"{N} is even number inclusive range 6 to 20")
    elif (2<=N<=5 and N%2==0):
        print (f"{N} is even number inclusive range 2 to 5")
    elif (N%2!=0):
        print (f"{N} is odd Number")
    else:
        print (f"{N} is even number")