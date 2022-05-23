''' 
Extracting the Age Population Pyramids
'''


# country also has pyramid
 
from . import config
import pandas as pd
import re 
from numpy import sum,where

num = re.compile(r'\d+')

def get_age(x):
    ''' 
    Get the age group from the pyramid columns

    ```
    input: ::str:: column name
    returns: ::int:: age
    ```
    '''
    return int(num.search(x)[0])



cols = []

def get_pyramid_data():
    ''' 
    Load the pyramids and split into sex, and years

    ```
    returns ::dict:: 
    ```
    
    '''
    global cols
    pyramids = {}
    for cat in config.CATEGORIES:
        header = 'PYRAMID' + getattr(config,cat+'_NAME')[1:]

        df = pd.read_csv(''.join([config.CSVTABLES,getattr(config,cat),config.simpletable['pyramid'],'.csv']),index_col=0,skip_blank_lines=True)
        # print(df)


        clist = list(set(map(lambda x: x.__str__().split(': ')[-1],df.columns)))
        clist.sort()
        cols.append(clist)

        pointysquare = []
        for sex in ['Females','Males']:

            columns =  list(filter(lambda x: sex in x,df.columns))
            columns.sort(key = get_age)
            pointysquare.append(df.loc[:,columns])


        pyramids[header] = pointysquare

    assert cols[0] == cols[-1] , ' lets make sure the tables have identical headers'
    cols = cols[0]

    return pyramids



pyramid_data = get_pyramid_data()



def get_pyramids(code):

    '''
    A function which returns the pyramid data for a given LAD 
    
    ```
    inputs: ::str:: code
    outputs: ::dict:: pyramid data
    ```
    
    '''


    pyramidd = dict([[i[0],[i[1][j].loc[code].values for j in [0,1]]] for i in pyramid_data.items()])

    agebands = {}

    for cat in config.CATEGORIES:
        header = 'PYRAMID' + getattr(config,cat+'_NAME')[1:]
        agegroup = 'LARGEST_AGEGROUP' + getattr(config,cat+'_NAME')[1:]


        combined = list(sum(pyramidd[header],axis=0))

        group = cols[combined.index(max(combined))]
        agebands[agegroup] = {'AGEBAND':get_age(group)}
        


    return dict(**pyramidd,**agebands)


