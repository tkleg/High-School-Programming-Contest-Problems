import random

choices = ['W', 'E']
for i in range(1, 16):
    with open("CountCrossings/input/input" + str(i).zfill(2) + ".txt", "w") as f:
        numSteps = random.randint(5, 30)
        f.write( str(numSteps) + "\n" )
        for j in range(numSteps):
            step = random.choice(choices)
            f.write(step + "\n")