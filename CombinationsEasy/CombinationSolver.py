import math

for i in range(1,16):
    fileNum = str(i).zfill(2)
    with open(f'CombinationsEasy/input/input{ fileNum }.txt', 'r') as f:
        batchSize, numItems = map(int, f.read().strip().split(' '))
    with open(f'CombinationsEasy/output/output{ fileNum }.txt', 'w') as f:
        f.write( str( math.comb(numItems, batchSize) ) )