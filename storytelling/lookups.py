'''
A file containing all the lokup tables used for generating the datasets

Contents:

    - A table outlining neighbouring areas in order of their significance
    - LAD codes to Region lookup table 
    - Translation of GeoCodes to Names

'''


import pandas as pd
from .config import DIR
from collections import defaultdict


# read neighbouring areas
neighbours = pd.read_csv(DIR + 'neighbours.csv') # column header not strictly true
neighbours = neighbours[neighbours.columns.sort_values()].set_index('LAD')

# lad to region lookup
lad2rgn = pd.read_csv(DIR + 'lad-rgn-ctry-lookup.csv').set_index('lad21cd')['rgn21cd'].to_dict()

# inverse dictionary of region lookup
rgn2lad = defaultdict(list)
for key, val in sorted(lad2rgn.items()):
    rgn2lad[val].append(key)

#  country lookup
lad2c = pd.read_csv(DIR + 'lad-rgn-ctry-lookup.csv').set_index('lad21cd')['ctry21cd'].to_dict()

# inverse dictionary
c2lad = defaultdict(list)
for key, val in sorted(lad2c.items()):
    c2lad[val].append(key)


# names lookup
names = pd.read_csv(DIR + 'code-name-lookup.csv').set_index('Code')['Name'].to_dict()



