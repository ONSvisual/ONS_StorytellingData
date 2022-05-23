
''' Neighbouring Functions '''
# from .population import population
from .lookups import names


def get_value(code:str):
    ''' 
    Gets the values for regions.
    This is calculated - yet unknown
```
    input: Geocode of a region
    output: ::dict:: The values for the region
    ```
    ''' 
    return dict(CODE=code,NAME = names[code], val='WHAT IS THIS VALUE')


nstats = {"last": -1,
"penultimate": -2,
"second": 1,
"top": 0}


def get_neigbours(row:list):
    ''' 
    Gets the neigbours for regions and populates the aray with their values.
    This follows the format provided in the nstats variable. 
```
    input: ::list:: Ranked list of neighbours
    output: ::dict::
    ```
    '''
    neighbours = row.to_list()
    return dict(CODES=neighbours,**dict([[k,get_value(neighbours[v])] for k,v in nstats.items()]))

    

''' End Neighbouring Functions '''