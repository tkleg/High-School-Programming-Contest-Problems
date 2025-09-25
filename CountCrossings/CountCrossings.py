for i in range(1, 16):
    with open("CountCrossings/input/input" + str(i).zfill(2) + ".txt", "r") as f:
            numSteps = int(f.readline().strip())
            steps = [f.readline().strip() for _ in range(numSteps)]
            curSide = steps[0]
            crossings = 0
            for step in steps[1:]:
                if step != curSide:
                    crossings += 1
                    curSide = step
    with open("CountCrossings/output/output" + str(i).zfill(2) + ".txt", "w") as f:
        f.write( str(crossings) )