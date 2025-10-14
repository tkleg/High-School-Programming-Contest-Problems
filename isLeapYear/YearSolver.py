for i in range(1, 8):
    fileNum = str(i).zfill(2)
    with open(f'isLeapYear/input/input{ fileNum }.txt', 'r') as f:
        year = int(f.read().strip())
    with open(f'isLeapYear/output/output{ fileNum }.txt', 'w') as f:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            f.write('Leap Year')
        else:
            f.write('Not a Leap Year')