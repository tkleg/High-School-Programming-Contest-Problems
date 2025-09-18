import random

for i in range(1, 16):
    fileNum = str(i).zfill(2)
    nonnums = ['X','-']
    nonnums_first_roll = nonnums[:]
    nonnums_second_roll = nonnums[1:]
    nums = [str(k) for k in range(1,10)]
    rolls = []
    while( rolls[-3:] != ['X','X','X'] ):
        rolls = []
        roll = None
        firstRoll = False
        extraRollsOnLastFrame = False
        numRoll = 1
        while( numRoll <= 20):
            while( numRoll <= 20 ):
                firstRoll = not firstRoll if roll != 'X' else True
                if( firstRoll ):
                    # Sample weights: X (strike) is less likely, '-' and numbers are more likely
                    choices_first = nonnums_first_roll + nums
                    weights_first = [10, 9] + [8]*len(nums)  # X:10, -:9, each number:8
                    roll = random.choices(choices_first, weights=weights_first, k=1)[0]
                else:
                    lastScore = int(rolls[-1]) if rolls[-1].isdigit() else 0
                    choices_second = nonnums_second_roll + [str(k) for k in range(1, 11 - int(lastScore))]
                    weights_second = [4] + [3]*(len(choices_second)-1)  # -:4, each number:3
                    roll = random.choices(choices_second, weights=weights_second, k=1)[0]
                rolls.append(roll)
                if roll == 'X':
                        if numRoll == 19 and not extraRollsOnLastFrame:
                            numRoll -= 1
                            extraRollsOnLastFrame = True
                        elif numRoll != 19:
                            numRoll += 1
                numRoll += 1
    with open("BowlingScoreEasy/input/input" + fileNum + ".txt", "w") as f:
        f.write(" ".join(rolls))