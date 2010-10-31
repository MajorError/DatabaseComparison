
__author__="majorerror"
__date__ ="$31-Oct-2010 09:42:52$"

from MySQLdb import *
from itemtypes import TYPES

DB = connect(user="root", db="3store")

def get_owner_names(owners):
    c = DB.cursor()
    c.execute('SELECT ownerid, Name FROM Owner WHERE ownerid IN (%s)' % ', '.join(owners))
    return dict([(str(o[0]), o[1]) for o in c.fetchall()])

def choose_owners(num=10):
    c = DB.cursor()
    c.execute("""SELECT DISTINCT Owner.ownerid FROM Owner
LEFT JOIN Item ON Owner.ownerid = Item.ownerid
GROUP BY Owner.ownerid
ORDER BY COUNT(itemid) DESC LIMIT %d""" % num)
    return [str(o[0]) for o in c.fetchall()]

def get_data_3store(owners):
    c = DB.cursor()
    c.execute("""SELECT Item.itemid, Item.type, ownerid, predicate, value
    FROM Item LEFT JOIN ItemDetails ON Item.itemid = ItemDetails.itemid
    WHERE Item.Ownerid IN (%s)""" % ', '.join(owners))
    data = {}
    for row in c.fetchall():
        itemid, type, ownerid, key, val = row
        if not key in TYPES[type]:
            continue
        if not str(ownerid) in data:
            data[str(ownerid)] = {}
        if not str(itemid) in data[str(ownerid)]:
            data[str(ownerid)][str(itemid)] = {}
            data[str(ownerid)][str(itemid)]['TYPE'] = type
        data[str(ownerid)][str(itemid)][key] = val
    return data

def get_data_rel(owners):
    c = DB.cursor()
    c.execute("""SELECT Item.itemid, type FROM Item WHERE Item.Ownerid IN (%s)""" % ', '.join(owners))
    items = {}
    for row in c.fetchall():
        itemid, type = row
        if not type in items:
            items[type] = []
        items[type].append(itemid)
    data = {}
    for type in items:
        keys = TYPES[type].keys()
        c = DB.cursor()
        c.execute('SELECT Item.itemid, ownerid, %s FROM Item LEFT JOIN %s ON Item.itemid = %s.itemid WHERE Item.itemid IN (%s)' %
            (', '.join(keys), type, type, ', '.join([str(x) for x in items[type]])))
        for row in c.fetchall():
            itemid = row[0]
            ownerid = row[1]
            if not str(ownerid) in data:
                data[str(ownerid)] = {}
            data[str(ownerid)][str(itemid)] = dict([(keys[i], row[i + 2]) for i in xrange(0, len(keys))])
            data[str(ownerid)][str(itemid)]['TYPE'] = type
    return data