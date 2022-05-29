'''
This file contains the configuration for the project.

- outfile
- directory
- excel to csv converted directory
- primary and secondary year file names
- translation of pnumbers to something readable


click view source to see the code.

'''

testing = False
print(__name__)

if testing: prefix = '../'
else: prefix = './'


import re,copy

OUTFILE =  prefix + 'output.json'
OUTDIR = './output'

DIR = prefix + 'data/'
CSVTABLES = DIR + 'fixedformatting/'

PRIMARY = 'census2011_Table-'
SECONDARY = 'midyear2020_rounded_Table-'

PY = re.search(r'20(\d{2})',PRIMARY)[1]
SY = re.search(r'20(\d{2})',SECONDARY)[1]

PRIMARY_NAME = 'Y' + PY
SECONDARY_NAME = 'Y' + SY


CATEGORIES = ['PRIMARY','SECONDARY']

simpletable = {
    'mf' : 'P01',
    'agebands' : 'P02',
    'pyramid' : 'P03',
    'density' : 'P04',
}


def diff(x:list):
    '''Subtraction function 
    ```input: ::list::
    output: ::element::
    ```
    '''
    dummy = x[-1]
    for i in range(0,len(x)-1):
        dummy -= x[i]
    return dummy 

def nest_select(elements,code):
    '''
    selects item from nested dict
    Max 4 layers deep. 
    '''
    ele = copy.deepcopy(elements)
    for i in ele:
        try:ele[i] = ele[i][code]
        except KeyError or AttributeError:
            for j in ele[i]:
                try: ele[i][j]= ele[i][j][code]
                except KeyError:
                    for k in ele[i][j]:
                        try: ele[i][j][k] = ele[i][j][k][code]
                        except KeyError:
                            print('missing',i,j,k,code)
                            ele[i][j][k] = None
                        

    return ele 

def nest_df(elements,code):
    '''
    selects item from nested dataframe
    Max 4 layers deep. 
    '''
    ele = copy.deepcopy(elements)

    for i in ele:
        try:ele[i] = ele[i].loc[code].values[0]
        except KeyError or AttributeError:
            for j in ele[i]:
                try: ele[i][j]= ele[i][j].loc[code].values[0]
                except KeyError:
                    for k in ele[i][j]:
                        try: ele[i][j][k] = ele[i][j][k].loc[code].values[0]
                        except KeyError:
                            print('missing',i,j,k,code)
                            ele[i][j][k] = None
                        

    return ele 


ENGLAND ='E92000011'
WALES = 'W92000004'


# '''
# %load_ext autoreload
# %autoreload 2
# '''