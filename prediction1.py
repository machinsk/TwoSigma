#!/usr/bin/env python
import pandas as pd
import numpy as np

with pd.HDFStore("train.h5", "r") as train:
    # Note that the "train" dataframe is the only dataframe in the file
    df = train.get("train")
    unique_ids = df['id'].unique()

    df2 = df[df['id'] == 10]
    df['ysum'] = df2['y'].cumsum()
    
    print df['ysum'][89086]
    #for x in unique_ids:
    #    df2 = df[df['id'] == x]
    #    #df['ysum' + str(x)] = df2['y'].cumsum()

        

    #df_2 = df[df['id'] == 10]