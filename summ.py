import pandas as pd
import numpy as np
from reading_spans import get_span as gs
import matplotlib.pyplot as plt
import seaborn as sns
from fine import Master as gm


class summary:

    def get_stats(df):
        #path=r'data.db'
        #spanid="ADL-ASI-4635-M-01-GR01-03"
        #df=gm.get_master(path,spanid)
        #print(df.info())
        #df.to_csv("Final.csv")
        for i in range(len(df)):
            if df['tnd_ot'][i]+df['tnd_hdd'][i]+df['hdd'][i]+df['dit'][i]+df['blow'][i]+df['drt'][i]+df['drt_duct_dam'][i]+df['dit_duct_miss'][i]==True:
                start=df['Chainage'][i]
                break

        for i in range(len(df)):
            if df['tnd_ot'][i]+df['tnd_hdd'][i]+df['hdd'][i]+df['dit'][i]+df['blow'][i]+df['drt'][i]+df['drt_duct_dam'][i]+df['dit_duct_miss'][i]==True:
                end=df['Chainage'][i]

        count_blow=0
        for i in range(len(df)):
            if df['blow'][i]==True:
                count_blow+=1

        count_dam=0
        for i in range(len(df)):
            if df['drt_duct_dam'][i]==True:
                count_dam+=1

        count_miss=0
        for i in range(len(df)):
            if df['dit_duct_miss'][i]==True:
                count_miss+=1

        count_dit=0
        for i in range(len(df)):
            if df['dit'][i]==True:
                count_dit+=1

        count_hdd=0
        for i in range(len(df)):
            if df['hdd'][i]==True:
                count_hdd+=1

        count_ot=0
        for i in range(len(df)):
            if df['tnd_ot'][i]==True:
                count_ot+=1

        chainage_start=start
        chainage_end=end
        span_len=end-start+1
        blo_len=count_blow
        duct_dam_len=count_dam
        duct_miss_len=count_miss
        dit_len=count_dit
        hdd_len=count_hdd
        ot_len=count_ot

        all_stats=[chainage_start,chainage_end,span_len,blo_len,duct_dam_len,duct_miss_len,dit_len,hdd_len,ot_len]
        df=df.loc[(df['Chainage']>=start) & (df['Chainage']<=end)]
        #print(df.info())
        return (df,all_stats)