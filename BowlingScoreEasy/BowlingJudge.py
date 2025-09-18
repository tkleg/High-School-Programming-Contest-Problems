for i in range(1, 16):
    with open("BowlingScoreEasy/input/input" + str(i).zfill(2) + ".txt", "r") as input_file:
        rolls = input_file.readline().strip().split(" ")
        score = sum( int(k) for k in rolls if k.isdigit())
        for index, roll in enumerate(rolls):
            if roll != 'X':
                continue
            score += 10
            if index + 1 < len(rolls):
                nextScore = rolls[index+1]
                if nextScore.isdigit():
                    score += int(nextScore)
                elif nextScore == 'X':
                    score += 10

                if index + 2 < len(rolls):
                    score_two_ahead = rolls[index+2]
                    if score_two_ahead.isdigit():
                        score += int(score_two_ahead)
                    elif score_two_ahead == 'X':
                            score += 10
    with open("BowlingScoreEasy/output/output" + str(i).zfill(2) + ".txt", "w") as f:
        f.write( str(score) )