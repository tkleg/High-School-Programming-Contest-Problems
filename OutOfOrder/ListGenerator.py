import random
import os

for i in range(1,11):
    fileNum = "0" + str(i) if i < 10 else str(i)
    with open("OutOfOrder/input/input"+fileNum+".txt", "w") as f:
        numLists = random.randint(1,10)
        f.write( str(numLists) + "\n" )
        for j in range(numLists):
            listSize = random.randint(1,20)
            randList = random.sample(range(1,100), listSize)
            f.write( " ".join(map(str, randList )) + "\n" )