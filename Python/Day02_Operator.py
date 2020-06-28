from DataInput import *
sampleInput = [x.replace("\n","") for x in inputMethod("Input/Day02_Operator.txt")]

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost*tip_percent/100
    tax = meal_cost*tax_percent/100
    total = meal_cost+tip+tax
    print(round(total))

if __name__ == '__main__':

    meal_cost = float(sampleInput[0])
    tip_percent = int(sampleInput[1])
    tax_percent = int(sampleInput[2])
    
    # Call method solve
    solve(meal_cost, tip_percent, tax_percent)

# output :
# 15