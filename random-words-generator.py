if __name__ == '__main__':
    inputFile = 'inputFile.txt'

from random_words import RandomWords
import numpy as np 
from textwrap import dedent

rm = RandomWords()
word = rm.random_words(count=5000)

n = 3
word = np.insert(word, range(n, len(word), n), "\n")
res = ' '.join(word)

f = open(inputFile, 'w')
f.writelines(res)
