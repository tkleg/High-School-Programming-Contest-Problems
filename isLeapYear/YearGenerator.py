import random

for i in range(1, 16):
    fileNum = str(i).zfill(2)
    with open(f'isLeapYear/input/input{ fileNum }.txt', 'w') as f:
        year = random.randint(1000, 3000)
        if i % 2 == 0: # Make some cases guaranteed to be leap years
            while( not((year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)) ):
                year = random.randint(1000, 3000)
        f.write(str(year))