for i in range(1, 16):
    fileNum = str(i).zfill(2)
    with open(f'Quadratic/input/input{ fileNum }.txt', 'r') as f:
        a, b, c = map(int, f.readline().strip().split())
        d = b**2 - 4*a*c
        print(a, b, c, d)
        with open(f'Quadratic/output/output{ fileNum }.txt', 'w') as f:
            if d >= 0:
                root1 = (-b + d**0.5) / (2*a)
                root2 = (-b - d**0.5) / (2*a)
                f.write(f'{root1:.2f} {root2:.2f}')
            else:
                f.write('Roots are complex')