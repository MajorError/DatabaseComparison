__author__="majorerror"
__date__ ="$30-Oct-2010 16:13:00$"

# Static set of types and their column types

TYPES = {'Pinatubo' : { 'TimeStamp' : 'datetime',
                        'Name' : 'words',
                        'Fact1' : 'string',
                        'Foo' : 'string',
                        'Bar' : 'number',
                        'Spoo' : 'float'},
         'Haleakala' : { 'TimeStamp' : 'datetime',
                        'Name' : 'words',
                        'Fact3' : 'string',
                        'SomeFoo' : 'string',
                        'Baz' : 'float',
                        'Spoo' : 'string',
                        'auxval1': 'bool',
                        'auxval2': 'bool',
                        'auxval3': 'bool',
                        'auxval4': 'bool',
                        'state1': 'bool',
                        'state2': 'bool'},
         'Pompeii' : { 'TimeStamp' : 'datetime',
                        'Name' : 'words',
                        'FactualInfo' : 'string',
                        'Spoo' : 'hex'},
         'Fuji' : { 'TimeStamp' : 'datetime',
                        'Name' : 'words',
                        'Fact1' : 'string',
                        'Foo' : 'words',
                        'Bar' : 'number',
                        'Spoo' : 'float',
                        'Spoo2' : 'float',
                        'Spoo3' : 'float',
                        'Spoo4' : 'words'}
        }