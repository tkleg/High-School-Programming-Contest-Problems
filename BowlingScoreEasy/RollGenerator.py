import random

nonnums = ['X','-']
nonnums_first_roll = nonnums[:]
nonnums_second_roll = nonnums[1:]
nums = [str(k) for k in range(1,10)]
for i in range(1,16):
    rolls = []
    roll = None
    numRoll = 1
    firstRoll = False
    extraRollsOnLastFrame = False
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
                print('strike rolled in file ' + str(i).zfill(2) + ' on roll ' + str(numRoll))
                if numRoll == 19 and not extraRollsOnLastFrame:
                    numRoll -= 1
                    extraRollsOnLastFrame = True
                elif numRoll != 19:
                    numRoll += 1
        numRoll += 1
    with open("BowlingScoreEasy/input/input" + str(i).zfill(2) + ".txt", "w") as f:
        f.write( " ".join(rolls) )
