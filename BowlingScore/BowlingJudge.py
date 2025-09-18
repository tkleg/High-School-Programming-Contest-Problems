for i in range(1, 16):
    fileNum = str(i).zfill(2)
    fileAllScores = []
    with open("BowlingScore/input/input" + fileNum + ".txt", "r") as input_file:
        numPlayers = int(input_file.readline().strip())
        for playerNum in range(numPlayers):
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
            fileAllScores.append((playerNum + 1, score))
    bestPlayerAndScore = max(fileAllScores, key=lambda x: x[1])
    with open("BowlingScore/output/output" + fileNum + ".txt", "w") as f:
        f.write( f"Player {bestPlayerAndScore[0]} wins with a score of {bestPlayerAndScore[1]}." )