from collections import Counter

for i in range(1,15):
    fileNum = "0" + str(i) if i < 10 else str(i)
    with open("MostCommonWord/input/input"+fileNum+".txt", "r") as fin:
        numLines = int(fin.readline().strip())
        word = ''
        for _ in range(numLines):
            line = fin.readline().strip()
            letter = Counter(line).most_common(1)[0][0]
            word += letter
        with open("MostCommonWord/output/output"+fileNum+".txt", "w") as fout:
            fout.write( word )
        print( word )
