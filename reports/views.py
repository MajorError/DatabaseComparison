from django.views.generic.simple import *
from dbquery import *
from itemtypes import get_type_keys

__author__="majorerror"
__date__ ="$31-Oct-2010 17:37:05$"

def hello(request):
    return direct_to_template(request, 'content.html',
            {'content':'Hello, World!\n\n%s' % request})

def static_init(request):
    owners = choose_owners(10)
    names = get_owner_names(owners)
    data = get_data_rel(owners)
    return direct_to_template(request, 'static_report.html',
            {'owners': owners,
             'names' : names,
             'types': get_type_keys(),
             'data': data
            })