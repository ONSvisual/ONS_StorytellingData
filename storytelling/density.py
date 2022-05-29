
import pandas as pd
from . import config
# import config
from .lookups import lad2rgn,names
import copy





def parent_region(x):
    ''' 
    Gets the parent region of the LAD code.

    ```
    input ::str:: x
    returns ::str::
    ```
    '''
    try:return lad2rgn[x]
    except KeyError: return None # it is the parent


def get_density_data():
    ''' 
        Gets the density of the country based on the PO4 tables for each year.

        This returns a groupby dataframe with a multiindex (region,code) and density as a value.

        ```
        returns ::DataFrame::
        ```
    '''

    ddensity = {}
    eextremes = {}
    for category in config.CATEGORIES:

        # density tables
        dty = pd.read_csv(''.join([config.CSVTABLES,getattr(config,category),config.simpletable['density'],'.csv']),index_col=0)

        # add region keys. 
        dty = pd.DataFrame(dty[dty.columns[-1]].values,index = dty.index)
        dty.columns=['density']


        # country extremes
        din = copy.deepcopy(dty).sort_values('density')
        #  skip zero valued
        din = din[din.density>0] 
        din['country'] = din.index.map(lambda x:x[0])
        eextremes[category] = din.groupby(by=['country']).apply(lambda x: x.sort_values(by='density').iloc[[0,-1]] )['density'].astype(int)

        # region groupings and density dataframe
        dty['region'] = list(map(parent_region,dty.index))
        ddensity[category] = dty.groupby(by=['region']).apply(lambda x: x.sort_values(by='density')['density'].astype(int))



    return [ddensity,eextremes]


density,extremes = get_density_data()



def get_density(code):
    ''' 
    Gets the density of the country based on the PO$ tables for each year.

    ```
    input ::str:: code
    returns ::rank::
    ```
    '''


    DENSITY = {}
    REGION_RANK = {'DENSITY':  {}}
    for category in config.CATEGORIES:

        # region = density[category].loc[:,code].index[0]
        region = lad2rgn[code]
        groupdf = copy.deepcopy(density)[category].loc[region]

        print('pp', groupdf)

        REGION_RANK['DENSITY'][getattr(config,category+'_NAME')]= {
            # reverse direction by subtracting from n items
                    "here": len(groupdf) - list(groupdf.index.values).index(code),
                    "all": len(groupdf)
                }
        

        DENSITY['DENSITY' + getattr(config,category+'_NAME')[1:] ] = density[category].loc[:,code].values[0]




    return  {"DENSITY": DENSITY,"REGION_RANK": REGION_RANK}


# print('E07000044',get_density('E07000044'))


def get_pitches(code):

    '''
    Calculate the football pitch extremes for a country. 
    This is done by dividing the density by 180 

    Currently this is done for the latest dataset only. 

    ```
    input ::str:: code
    returns ::dict:: football pitch extremes
    ```
    
    '''

    global extremes

    cat = 'SECONDARY'

    data = copy.deepcopy(extremes)[cat].loc[code[0]].to_dict()
    codes = list(data.keys())
    values = list(data.values())

    return {
                "highest": {
                    "LAD": codes[1],
                    "NAME": names[codes[0]],
                    "PEOPLE_PER_FOOOTY_PITCH": '%.4f'%(values[1]/180)
                },
                "lowest": {
                    "LAD": codes[0],
                    "NAME": names[codes[0]],
                    "PEOPLE_PER_FOOOTY_PITCH": '%.4f'%(values[0]/180 )
                }
            }


