from Input.DataInput import *
sampleInput = inputMethod("Input/Day04_Class_vs_Instance.txt")


class Person:
    def __init__(self,initialAge):
        if initialAge > 0 :
            self.age = initialAge
        else:
            print('Age is not valid, setting age to 0.')
            self.age = 0
    def amIOld(self):
        if self.age < 13 :
            print('You are young.')
        elif 13 <= self.age < 18 :
            print ('You are a teenager.')
        else:
            print('You are old.')
    def yearPasses(self):
        self.age += 1


for i in range(1, int(sampleInput[0])+1):
    age = int(sampleInput[i])         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")


# expected output :

# Age is not valid, setting age to 0.
# You are young.
# You are young.

# You are young.
# You are a teenager.

# You are a teenager.
# You are old.

# You are old.
# You are old.