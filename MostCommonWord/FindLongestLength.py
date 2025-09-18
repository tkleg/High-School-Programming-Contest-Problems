maxLength = 0
for i in range(1,15):
    fileNum = "0" + str(i) if i < 10 else str(i)
    with open("MostCommonWord/input/input"+fileNum+".txt", "r") as f:
        for line in f.readlines():
            maxLength = max( maxLength, len(line) )

print( maxLength )