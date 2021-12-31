# Use product to get all combinations between two iterators

import itertools
import random
import sys
import time
import string

# from Fluent Python
ranks = [str(n) for n in range(2, 11)] + list('JQKA')
suits = 'S D C H'.split() # spades diamonds clubs hearts
# but instead of double list comprehension, using product
cards = ['{}{}'.format(*p) for p in itertools.product(suits, ranks)]
print(cards)

#Combinations and permutations
letters = random.sample(string.ascii_uppercase, 7)
print(len(list(itertools.permutations(letters, 4))))

#Show a progress spinner for a console app

def spinner(seconds):
    """Show an animated spinner while we sleep."""
    symbols = itertools.cycle('-|/')
    tend = time.time() + seconds
    while time.time() < tend:
        # 'r' is carriage return: return cursor to the start of the line.
        sys.stdout.write('\rPlease wait... ' + next(symbols)) # no newline
        sys.stdout.flush()
        time.sleep(0.1)
    print() # newline

if __name__ == "__main__":
    spinner(3)


