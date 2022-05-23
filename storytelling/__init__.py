'''
Welcome to the StoryTelling documentation.

This consists of a series of functions that are used to generate the story dataset. 
To view the main script go to <a href="./storytelling/__main__.html">__main__.py</a> and select "View source".


-----------------------------------------------------
-----------------------------------------------------
'''

from . import config
from . import lookups
from .population import get_LA_population
from .neighbours import get_neigbours
from .pyramid import get_pyramids
# __all__ = [lookups,get_value','get_neigbours




#  handle int65 
import numpy as np
import json

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

