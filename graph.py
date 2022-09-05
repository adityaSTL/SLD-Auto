import pandas as pd
import numpy as np
from reading_spans import get_span as gs
import matplotlib.pyplot as plt
import seaborn as sns
from fine import Master as gm
from summ import summary

class plot:
    def get_plot(df):
        z=df.loc[df['hdd']==True,['Chainage']]
        plt.plot(z['Chainage'],[2]*len(z),'o',color='grey',label="HDD")

        z=df.loc[df['tnd_ot']==True,['Chainage']]
        plt.plot(z['Chainage'],[3]*len(z),'o',color='green')

        z=df.loc[df['drt']==True,['Chainage']]
        plt.plot(z['Chainage'],[4]*len(z),'o',color='black')

        z=df.loc[df['drt_duct_dam']==True,['Chainage']]
        plt.plot(z['Chainage'],[5]*len(z),'o',color='red')

        z=df.loc[df['dit_duct_miss']==True,['Chainage']]
        plt.plot(z['Chainage'],[6]*len(z),color='blue')

        z=df.loc[df['dit']==True,['Chainage']]
        plt.plot(z['Chainage'],[7]*len(z),'o',color='yellow')

        z=df.loc[df['blow']==True,['Chainage']]
        plt.plot(z['Chainage'],[8]*len(z),'o',color='orange')

        
        #df.plot(kind='scatter',x=z,y=[2]*len(z),color='red')
        plt.show()