for i in range(1, 16):
    with open("AlternatingFibbonaciSum/input/input" + str(i).zfill(2) + ".txt", "r") as f:
        n, evenScaler, oddScaler = map(int, f.readline().strip().split(" "))
        fib = [0, 1]
        for j in range(2, n):
            fib.append(fib[-1] + fib[-2])
        print(fib)
        total = 0
        for idx, v in enumerate(fib):
            idx = idx + 1
            if idx % 2 == 0:
                total += v * evenScaler
            else:
                total += v * oddScaler
    with open("AlternatingFibbonaciSum/output/output" + str(i).zfill(2) + ".txt", "w") as f:
        f.write( str(total) )