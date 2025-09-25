import random

for i in range(1, 16):
    with open("AlternatingFibbonaciSum/input/input" + str(i).zfill(2) + ".txt", "w") as f:
        n = random.randint(5, 15)
        evenScaler = random.randint(2, 10)
        oddScaler = random.randint(2, 10)
        f.write( str(n) + " " + str(evenScaler) + " " + str(oddScaler) + "\n" )