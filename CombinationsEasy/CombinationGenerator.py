import random

for i in range(1,16):
    fileNum = str(i).zfill(2)
    with open(f'CombinationsEasy/input/input{ fileNum }.txt', 'w') as f:
        batchSize = random.randint(2,10)
        f.write( str(batchSize) + ' ' )
        numItems = random.randint(batchSize, batchSize*5)
        f.write( str(numItems) )