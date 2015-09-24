import sys
import random


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('You must pass the number of words to use.')
    else:
        with open('/usr/share/dict/words', 'r') as document:
            words = document.read().splitlines()
            print(' '.join(random.sample(words, int(sys.argv[1]))))
