import random

testCasesComplex = random.sample(range(1, 8), 1)
print("Test cases with complex roots:", testCasesComplex)
for i in range(1, 8):
    fileNum = str(i).zfill(2)
    with open(f'Quadratic/input/input{ fileNum }.txt', 'w') as f:
        a = random.randint(5, 25)
        b = random.randint(5, 25)
        max_c = (b**2) // (4*a)
        if i not in testCasesComplex:
            c = random.randint(max_c-10, max_c)
        else:
            c = random.randint(max_c+1, max_c+10)
        if i == 5:
            a = 0
        if i == 4:
            b = 5
            c = 38
            a = 24
        f.write(f'{a} {b} {c}')