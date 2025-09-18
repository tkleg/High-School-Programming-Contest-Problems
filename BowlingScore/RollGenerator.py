import random

nonnums = ['X','-']
nonnums_first_roll = nonnums[:]
nonnums_second_roll = nonnums[1:]
nums = [str(k) for k in range(1,10)]
for i in range(1,16):
    fileNum = str(i).zfill(2)
    allScores = []
    numScores = random.randint(2, 10)
    with open("BowlingScore/input/input" + fileNum + ".txt", "w") as f:
        f.write( str(numScores) + "\n" )
    for scoreNum in range(0, numScores):
        rolls = []
        roll = None
        numRoll = 1
        firstRoll = False
        while( numRoll <= 20 ):
            firstRoll = not firstRoll if roll != 'X' else True
            tempChoices = []
            if( firstRoll ):
                tempChoices = nonnums_first_roll + nums
                roll = random.choice(tempChoices)
            else:
                lastScore = int(rolls[-1]) if rolls[-1].isdigit() else 0
                tempChoices = nonnums_second_roll + [str(k) for k in range(1, 11 - int(lastScore))]
                roll = random.choice(tempChoices)
            rolls.append(roll)
            numRoll += 1
            if roll == 'X':
                numRoll += 1
        allScores.append(rolls)
    with open("BowlingScore/input/input" + fileNum + ".txt", "a") as f:
        for rolls in allScores:
            f.write( " ".join(rolls) + "\n" )
