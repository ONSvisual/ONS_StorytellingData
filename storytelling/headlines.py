'''
Calculate the headline data from the population group datafarame for a specific column '''

from .population import population, population_delta
from .population import pop_group as p
from .lookups import names
from . import config

import pandas as pd
COL = 'COUNTRY'





# grouped = []
# for cat in config.CATEGORIES:
#     grouped.append( p[cat].sort_values(0).groupby(COL).apply(lambda x: x[0]) )


def summary_selection(code):

    return {
                        "LAD": code,
                        "NAME": names[code],
                        f"POP{config.PY}": int(population['PRIMARY'].loc[code]),
                        f"POP{config.SY}": int(population['SECONDARY'].loc[code]),
                        "CHANGE": population_delta[code]
                    }




def get_headline_data(df):

    # abs change 

    abs_change = pd.DataFrame(df.sort_values('PC_CHANGE',ascending=False)['PC_CHANGE']).dropna()



    return       {
            "BIGGEST_POP_CHANGE_UP": {
                "top": summary_selection(abs_change.index[0]),
                "second": summary_selection(abs_change.index[1])
            },
            "BIGGEST_POP_CHANGE_DOWN": {
                "lowest": summary_selection(abs_change.index[-1]),
                "second_lowest": summary_selection(abs_change.index[-2])
                }
        }

