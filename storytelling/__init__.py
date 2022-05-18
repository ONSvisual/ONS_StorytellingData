'''
Welcome to the StoryTelling documentation.

This consists of a series of functions that are used to generate the story dataset. 
To view the main script go to <a href="./storytelling/__main__.py">__main__.py</a> and select "View source".

'''


from . import lookups
# __all__ = [lookups,get_value','get_neigbours']

config = {
    'OUTFILE' : './output.json',
}



''' Neighbouring Functions '''

def get_value(code:str):
    ''' 
    Gets the values for regions.
    This is calculated - yet unknown

    input: Geocode of a region
    ''' 
    return dict(CODE=code,NAME = lookups.names[code], val='...')


nstats = {"last": -1,
"penultimate": -2,
"second": 1,
"top": 0}


def get_neigbours(row:list):
    ''' 
    Gets the neigbours for regions and populates the aray with their values.
    This follows the format provided in the nstats variable. 

    input: Ranked list of neighbours
    
    '''
    neighbours = row.to_list()
    return dict(CODES=neighbours,**dict([[k,get_value(neighbours[v])] for k,v in nstats.items()]))

    

''' End Neighbouring Functions '''