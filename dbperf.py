
__author__="majorerror"
__date__ ="$30-Oct-2010 15:18:05$"

from datageneration import generate
from database import insert
from dbquery import *
from timeit import Timer

if __name__ == "__main__":
    #for x in generate(1000000):
    #    insert(x)
    owners = choose_owners()
    print '>> 3store:      %s' % Timer('from __main__ import get_data_3store as f; f(%s)' % owners).repeat(5, 100)
    print '>> relational:  %s' % Timer('from __main__ import get_data_rel as f; f(%s)' % owners).repeat(5, 100)
    d1 = get_data_3store(owners)
    d2 = get_data_rel(owners)
    print 'D1.keys - D2.keys: %s' % (set(d1.keys()) - set(d2.keys()))
    print 'D2.keys - D1.keys: %s' % (set(d2.keys()) - set(d1.keys()))
    for owner in d1:
        a = d1[owner]
        b = d2[owner]
        if len(set(a.keys()) - set(b.keys())) > 0:
            print 'a.keys - b.keys: %s' % (set(a.keys()) - set(b.keys()))
        if len(set(b.keys()) - set(a.keys())) > 0:
            print 'b.keys - a.keys: %s' % (set(b.keys()) - set(a.keys()))
        for item in a:
            ia = a[item]
            ib = b[item]
            print 'Check %s -> %s of type %s' % (owner, item, ia['TYPE'])
            if len(set(ia.keys()) - set(ib.keys())) > 0:
                print 'ia.keys - ib.keys: %s' % (set(ia.keys()) - set(ib.keys()))
            if len(set(ib.keys()) - set(ia.keys())) > 0:
                print 'ib.keys - ia.keys: %s' % (set(ib.keys()) - set(ia.keys()))
            for pred in ia.keys():
                if not pred in ib:
                    continue
                if not str(ia[pred]) == str(ib[pred]):
                    print '\t%s: %s != %s' % (pred, str(ia[pred]), str(ib[pred]))
