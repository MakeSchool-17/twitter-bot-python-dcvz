import sys
import random


def reassemble_words(array):
    random.shuffle(array)
    return array

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('You must at least pass two words as arguments.')
    else:
        args = reassemble_words(sys.argv[1:])
        print(' '.join(args))
