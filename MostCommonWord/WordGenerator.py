import random
from collections import Counter
from random_word import RandomWords
import string

randGenerator = RandomWords()

def nLetterWord( n ):
    rand5Letter = randGenerator.get_random_word()
    while( len(rand5Letter) != n ):
        rand5Letter = randGenerator.get_random_word()
    return rand5Letter.lower()

for i in range(1,15):
    fileNum = "0" + str(i) if i < 10 else str(i)
    with open("MostCommonWord/input/input"+fileNum+".txt", "w") as f:
        numLines = random.randint(3,10)
        randWord = nLetterWord(numLines)
        print( numLines, randWord )
        f.write( str(numLines) + "\n" )
        for j in range(numLines):
            charForLine = randWord[j]
            lineSize = random.randint(50,100)
            randLine = ''.join(random.choices(string.ascii_lowercase, k=lineSize))
            while( Counter(randLine).most_common(1)[0][0] != charForLine ):
                randLine += charForLine
            randLine += charForLine
            randLineList = list(randLine)
            random.shuffle( randLineList )
            randLine = ''.join( randLineList )
            f.write( randLine + "\n" )