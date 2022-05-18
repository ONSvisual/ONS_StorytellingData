'''
A file containing all the lokup tables used for generating the datasets

Contents:

    - A table outlining neighbouring areas in order of their significance
    - LAD codes to Region lookup table 
    - Translation of GeoCodes to Names

'''


import pandas as pd

# read neighbouring areas
neighbours = pd.read_csv('./data/neighbours.csv') # column header not strictly true
neighbours = neighbours[neighbours.columns.sort_values()].set_index('LAD')

# lad to region lookup
lad2rgn = pd.read_csv('./data/lad-rgn-ctry-lookup.csv').set_index('lad21cd')['rgn21cd'].to_dict()

# names lookup
names = pd.read_csv('./data/code-name-lookup.csv').set_index('Code')['Name'].to_dict()
