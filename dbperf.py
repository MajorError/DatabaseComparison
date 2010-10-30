
__author__="majorerror"
__date__ ="$30-Oct-2010 15:18:05$"

from datageneration import generate
from database import insert

if __name__ == "__main__":
    for x in generate(1000000):
        insert(x)
