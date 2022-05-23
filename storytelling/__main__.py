'''
The main programme file for the project.
'''


from .__init__ import * 

from tqdm import tqdm
import json as JSON


json = []


#  loop over neighbours
for cid , row  in tqdm(list(lookups.neighbours.iterrows())):

    if cid[0] == 'E':
        COUNTRY_CODE = 'E92000011'
        COUNTRY_NAME = 'England'
        WALES = 0 

    elif cid[0] == 'W':
        COUNTRY_CODE = 'W92000004'
        COUNTRY_NAME = 'Wales'
        WALES = 1


    LA = {** get_LA_population(cid),}

    dummy = dict(CODE = cid, NAME = lookups.names[cid], REGION_CODE =  lookups.lad2rgn[cid] , REGION_NAME=lookups.names[lookups.lad2rgn[cid]] , COUNTRY_CODE = COUNTRY_CODE, COUNTRY_NAME = COUNTRY_NAME, WALES = WALES, NEIGHBOURS = get_neigbours(row),LA=LA,PYRAMIDS = get_pyramids(cid))


    json.append(dummy)




# write the dict to a json file
print('Writng to :',config.OUTFILE)
JSON.dump(json, open(config.OUTFILE,'w'),cls=NpEncoder,indent=4)
