for i in range(1,11):
    fileNum = "0" + str(i) if i < 10 else str(i)
    with open("OutOfOrder/input/input"+fileNum+".txt", "r") as f:
        lines = f.readlines()
        numLists = int(lines[0].strip())
        lines = lines[1:]
        lists = [list(map(int, line.strip().split())) for line in lines]
        with open("OutOfOrder/output/output"+fileNum+".txt", "w") as out:
            for curList in lists:
                curValidList = []
                curOutOfOrderList = []
                for num in curList:
                    if len(curValidList) == 0 or num > curValidList[-1]:
                        curValidList.append(num)
                    else:
                        curOutOfOrderList.append(num)
                out.write( " ".join(map(str, curOutOfOrderList)) + "\n" )