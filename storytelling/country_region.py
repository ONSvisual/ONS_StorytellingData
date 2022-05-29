'''
This file concerns itself with the creation of the country and region sections of the tables. 

These contain: 
- abs
- abs change
- pc change 
- j20 
- o65
- working
- pyramids
- largest agegroup
- headlines

'''


from . import config 
from .population import pop_group,population
from .lookups import rgn2lad,c2lad
from .headlines import get_headline_data, summary_selection
from .pyramid import get_pyramids
from .config import nest_df as nest_select
selections = ['COUNTRY','REIGION']


''' Starting the Grouped Population Stats for country and region'''





def get_grouped_stats(column:str,filtarr=False,pg=pop_group):
    '''
    Generate a group of stats (abs, abs change, and pc change) from a column, e.g. Country or Region. 

    ```
    inputs: ::str:: column name
            ::list:: filter list to apply 
    outputs: ::dict:: (nested)
    ```
    '''
    if filtarr:

        # filtarr = list(filter(lambda x: x not in pop_group['PRIMARY'].index.values, filtarr))

        ABS = {config.PRIMARY_NAME:pg['PRIMARY'].loc[filtarr,0], config.SECONDARY_NAME:pg['SECONDARY'].loc[filtarr,0]}
    else:
        ABS = {config.PRIMARY_NAME:pop_group['PRIMARY'].groupby(column).sum(), config.SECONDARY_NAME:pop_group['SECONDARY'].groupby(column).sum()}


    ABS_CHANGE = {f'FROM{config.PRIMARY_NAME[1:]}TO{config.SECONDARY_NAME[1:]}':config.diff(list(ABS.values())).sort_values(0,ascending=False)}

    PC_CHANGE = {f'FROM{config.PRIMARY_NAME[1:]}TO{config.SECONDARY_NAME[1:]}':list(ABS_CHANGE.values())[0]/ABS[config.PRIMARY_NAME]*100}

    return dict(ABS=ABS,ABS_CHANGE=ABS_CHANGE,PC_CHANGE=PC_CHANGE)






rstats = [get_grouped_stats(rg,cds) for rg,cds in rgn2lad.items()]



rdstats = dict(zip(rgn2lad.keys(),rstats))
rheadlines = dict(zip(rgn2lad.keys(),list(map(get_headline_data,rstats))))

cstats = [get_grouped_stats(ct,cds) for ct,cds in c2lad.items()]
cheadlines = dict(zip(c2lad.keys(),list(map(get_headline_data,cstats))))


region_change = [summary_selection(r) for r in rgn2lad.keys() if str(r) != 'nan']

country_change = [summary_selection(r) for r in c2lad.keys() if str(r) != 'nan']


country_pyramids = dict([[c,get_pyramids(c)] for c in c2lad.keys() if str(c) != 'nan'])



