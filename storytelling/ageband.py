import pandas as pd

from . import config
# from .config import nest_select

import re 
fnum = re.compile(r'(\d+)')


def get_ages():
    '''
    Get the age groups from the relevant file
    '''
    ages = {}
    for category in config.CATEGORIES:
        #
        df = pd.read_csv(''.join([config.CSVTABLES,getattr(config,category),config.simpletable['agebands'],'.csv']),index_col=0)

        df = df.loc[:,df.columns.str.contains('Age')]
        df.columns = [int(fnum.search(i)[1]) for i in df.columns]

        ages[category] = df

    return ages


ages = get_ages()


def get_agegroups():
    '''
    Get the age groups from the relevant file
'''
    
    agebands = {'UNDER20':{'ABS':{},'PC':{}},'OVER65':{'ABS':{},'PC':{}},'WORKING':{'ABS':{},'PC':{}}}

    for category in config.CATEGORIES:

        j20 = ages[category].loc[:, ages[category].columns<20].sum(axis=1)
        o65 = ages[category].loc[:, ages[category].columns>=65].sum(axis=1)


        total = ages[category].sum(axis=1)
        working = total-j20-o65
        
        #  abs counts
        agebands['UNDER20']['ABS'][getattr(config,category+'_NAME')] = j20.to_dict()
        agebands['OVER65']['ABS'][getattr(config,category+'_NAME')] = o65.to_dict()
        agebands['WORKING']['ABS'][getattr(config,category+'_NAME')] = working.to_dict()

        #  percentage of total
        agebands['UNDER20']['PC'][getattr(config,category+'_NAME')] = (j20.divide(total)*100).round(decimals=2).to_dict()
        agebands['OVER65']['PC'][getattr(config,category+'_NAME')] = (o65.divide(total)*100).round(decimals=2).to_dict()
        agebands['WORKING']['PC'][getattr(config,category+'_NAME')] = (working.divide(total)*100).round(decimals=2).to_dict()

        

    return agebands


agebands = get_agegroups()


