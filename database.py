__author__="majorerror"
__date__ ="$30-Oct-2010 15:31:41$"

from MySQLdb import *
from random import randint
from time import time

DB = connect(user="root", db="3store")

def get_id(name):
    c = DB.cursor()
    c.execute('SELECT ownerid FROM Owner WHERE name = %s', (name,))
    for id in c.fetchall():
        return id[0]
    return -1

def random_owner():
    c = DB.cursor()
    c.execute('SELECT ownerid FROM Owner ORDER BY Rand() LIMIT 1')
    for id in c.fetchall():
        return id[0]

def item_3store(id, item):
    print '3store adding item %s' % id
    values = []
    for key in item:
        values.append((id, key, item[key]))
    c = DB.cursor()
    c.executemany('INSERT INTO ItemDetails (itemid, predicate, value) VALUES (%s, %s, %s)', values)

def item_relational(id, item):
    print 'relational adding item %s' % id
    keys = item.keys()
    keys.remove('TYPE')
    values = [item[k] for k in keys]
    # Manually set id so they're consistent
    keys.append('itemid')
    values.append(id)
    c = DB.cursor()
    c.execute('INSERT INTO %s (%s) VALUES (%s)' % (item['TYPE'], ', '.join(keys), ', '.join(['%s'] * len(values))), tuple(values))

def create_owner(name):
    c = DB.cursor()
    c.execute('INSERT INTO Owner (name, description) VALUES (%s, %s)', (name, '{Default}'))
    return c.lastrowid

def insert(item):
    if randint(0, 10) > 2:
        owner = random_owner()
    else:
        owner = get_id(item['Name'])
    if owner < 0:
        owner = create_owner(item['Name'])
    c = DB.cursor()
    c.execute('INSERT INTO Item (ownerid,type) VALUES (%s, %s)', (owner, item['TYPE']))
    id = c.lastrowid
    item_3store(id, item)
    item_relational(id, item)

if __name__ == "__main__":
    DB.cursor().execute("""DROP TABLE IF EXISTS `Item`;
CREATE TABLE `Item` (
  `itemid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `ownerid` int(10) unsigned NOT NULL,
  `type` char(64) NOT NULL,
  PRIMARY KEY (`itemid`)
) ENGINE=MyISAM AUTO_INCREMENT=622061 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `ItemDetails`;
CREATE TABLE `ItemDetails` (
  `itemid` int(10) unsigned NOT NULL,
  `predicate` varchar(64) NOT NULL,
  `value` varchar(255) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  KEY `pred` (`predicate`),
  KEY `val` (`value`),
  KEY `time` (`timestamp`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 PACK_KEYS=1;

DROP TABLE IF EXISTS `Owner`;
CREATE TABLE `Owner` (
  `OwnerID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) NOT NULL,
  `Description` varchar(1024) NOT NULL,
  PRIMARY KEY (`OwnerID`)
) ENGINE=MyISAM AUTO_INCREMENT=170138 DEFAULT CHARSET=latin1;""")
    from itemtypes import TYPES
    map =    {'words': 'VARCHAR(255)',
              'string': 'VARCHAR(255)',
              'hex': 'VARCHAR(64)',
              'datetime': 'TIMESTAMP',
              'number': 'INT',
              'float': 'DECIMAL(65,20)',
              'bool': 'BOOL'
             }
    for t in TYPES:
        type = TYPES[t]
        cols = ['itemid INT UNSIGNED NOT NULL']
        for key in type:
            cols.append('%s %s NOT NULL' % (key, map[type[key]]))
        c = DB.cursor()
        c.execute('DROP TABLE IF EXISTS %s' % t)
        c = DB.cursor()
        c.execute('CREATE TABLE %s (%s) ENGINE = MyISAM' % (t, ','.join(cols)))