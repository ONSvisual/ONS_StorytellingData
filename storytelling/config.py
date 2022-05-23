testing = False
print(__name__)

if testing: prefix = '../'
else: prefix = './'


import re

OUTFILE =  prefix + 'output.json'

DIR = prefix + 'data/'
CSVTABLES = DIR + 'fixedformatting/'

PRIMARY = 'census2011_Table-'
SECONDARY = 'midyear2020_rounded_Table-'

PRIMARY_NAME = 'Y' + re.search(r'20(\d{2})',PRIMARY)[1]
SECONDARY_NAME = 'Y' + re.search(r'20(\d{2})',SECONDARY)[1]

CATEGORIES = ['PRIMARY','SECONDARY']

simpletable = {
    'mf' : 'P01',
    'agebands' : 'P02',
    'pyramid' : 'P03',
    'density' : 'P04',
}





'''
%load_ext autoreload
%autoreload 2
'''