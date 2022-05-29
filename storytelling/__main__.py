'''
The main programme file for the project.
'''


from asyncio import FastChildWatcher
from .__init__ import *

from tqdm import tqdm
import json as JSON


json = []


#  loop over neighbours
for cid , row  in tqdm(list(lookups.neighbours.iterrows())):

    try:

        # print('----TEST_----')
        # cid = 'E07000044'
        # row = lookups.neighbours.loc[cid]

        if cid[0] == 'E':
            COUNTRY_CODE = 'E92000001'
            COUNTRY_NAME = 'England'
            WALES = 0

        elif cid[0] == 'W':
            COUNTRY_CODE = 'W92000004'
            COUNTRY_NAME = 'Wales'
            WALES = 1

        LA = {**get_population(cid),** nest_select(agebands,cid),**get_pyramids(cid)}

        REGION_CODE = lookups.lad2rgn[cid]
        REGION = dict(**get_population(REGION_CODE,False),HEADLINES = rheadlines[REGION_CODE],REGION_CHANGE = region_change)


        COUNTRY = dict(**get_population(COUNTRY_CODE,False), ** nest_select(agebands,COUNTRY_CODE),**country_pyramids[COUNTRY_CODE], HEADLINES = {**cheadlines[COUNTRY_CODE],'FOOTBALL_PITCH_EXTREMES': get_pitches(COUNTRY_CODE)})
        # HEADLINES = 
        # **get_population(COUNTRY_CODE,False)

        dummy = dict(CODE = cid, NAME = lookups.names[cid], REGION_CODE =  REGION_CODE , REGION_NAME=lookups.names[lookups.lad2rgn[cid]] , COUNTRY_CODE = COUNTRY_CODE, COUNTRY_NAME = COUNTRY_NAME, WALES = WALES, NEIGHBOURS = get_neigbours(row),LA=LA, REGION = REGION)
        


        



        json.append(dummy)
        # break


        # write the dict to a json file
        # print('Writng to :',config.OUTDIR,lookups.names[cid],cid)

        JSON.dump(json[-1], open(f'{config.OUTDIR}/{cid}.json','w'),cls=NpEncoder,indent=4)


    except ValueError as e:
        print(e)
        print('ValueError with :',cid, lookups.names[cid])
        continue
    except KeyError as e:
        # print(e)
        print('KeyError with :',cid, lookups.names[cid],(e),'skipping')
        continue


# print(JSON.dumps(json,cls=NpEncoder,indent = 4))