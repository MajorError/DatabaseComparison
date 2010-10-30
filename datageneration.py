__author__="majorerror"
__date__ ="$30-Oct-2010 15:31:34$"

import string
from datetime import datetime
from random import choice, randint

from itemtypes import TYPES

# Meat of the generation happens in these lambda functions
GENERATORS = {'words': lambda: ''.join(choice(string.letters + '    -_') for x in xrange(randint(10, 20))),
              'string': lambda: ''.join(choice(string.printable) for x in xrange(randint(10, 65))),
              'hex': lambda: ''.join(choice(string.hexdigits) for x in xrange(randint(1, 32))),
              'datetime': lambda: datetime(randint(1990, 2010), randint(1, 12),
                randint(1, 28), randint(0, 23), randint(0, 59), randint(0, 59)),
              'number': lambda: randint(0, 999999),
              'float': lambda: randint(0, 10000000) / 1000.00,
              'bool': lambda: randint(0, 1) == 0
             }

def generate(numvals=10):
    for i in xrange(0, numvals):
        type = TYPES.keys()[randint(0, len(TYPES.keys()) - 1)]
        output = {'TYPE': type}
        for key in TYPES[type]:
            output[key] = GENERATORS[TYPES[type][key]]()
        yield output
        