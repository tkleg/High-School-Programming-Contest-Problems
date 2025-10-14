import random
import os

for i in range(1,6):
    fileNum = "0" + str(i) if i < 10 else str(i)
    with open("OutOfOrder/input/input"+fileNum+".txt", "w") as f:
        numLists = random.randint(1,10)
        if i == 4:
            numLists = 10 # edge case ( sorted list )
        elif i == 5:
            numLists = 1 # edge case ( min size )
        elif i == 3:
            numLists = 10 # edge case ( max size )

        f.write( str(numLists) + "\n" )
        for j in range(numLists):
            listSize = random.randint(1,20)
            if i == 5:
                listSize = 1
            elif i == 3:
                listSize = 20 # edge case ( max size )
            randList = random.sample(range(1,100), listSize)
            if i == 4 and j == 1:# edge case ( sorted list )
                randList.sort()
            f.write( " ".join(map(str, randList )) + "\n" )