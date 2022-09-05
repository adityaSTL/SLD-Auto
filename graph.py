import pandas as pd
import numpy as np
from reading_spans import get_span as gs
import matplotlib.pyplot as plt
import seaborn as sns
from fine import Master as gm
from summ import summary

class plot:
    def get_plot(spanid,df):

        fig, ax = plt.subplots()
        z=df.loc[df['hdd']==True,['Chainage']]
        y=df.loc[df['hdd_marker']]
        plt.plot(z['Chainage'],[2]*len(z),'o',color='grey',label="HDD",alpha=1,markersize=2)
        plt.plot(y['Chainage'],[2]*len(y),'|',color='grey',markersize=20,alpha=0.3)

        z=df.loc[df['tnd_ot']==True,['Chainage']]
        y=df.loc[df['tnd_ot_marker']==True,['Chainage']]
        plt.plot(z['Chainage'],[2]*len(z),'o',color='green',label="OT",alpha=0.7,markersize=3.5)
        plt.plot(y['Chainage'],[2]*len(y),'|',color='green',markersize=20,alpha=0.3)

        z=df.loc[df['drt']==True,['Chainage']]
        y=df.loc[df['drt_marker']==True,['Chainage']]
        plt.plot(z['Chainage'],[2]*len(z),'o',color='blue',label="DRT",alpha=0.3,markersize=5)
        plt.plot(y['Chainage'],[2]*len(y),'|',color='blue',markersize=20,alpha=0.3)

        z=df.loc[df['drt_duct_dam']==True,['Chainage']]
        y=df.loc[df['drt_duct_dam_marker']==True,['Chainage']]
        plt.plot(z['Chainage'],[3]*len(z),'o',color='brown',label="Duct_Dam",alpha=0.4,markersize=5)
        plt.plot(y['Chainage'],[3]*len(y),'|',color='brown',markersize=20,alpha=0.3)

        z=df.loc[df['dit_duct_miss']==True,['Chainage']]
        y=df.loc[df['dit_duct_miss_marker']==True,['Chainage']]
        plt.plot(z['Chainage'],[3]*len(z),'o',color='black',label="Duct_Miss",alpha=1,markersize=3)
        plt.plot(y['Chainage'],[3]*len(y),'|',color='black',markersize=15,alpha=0.3)

        z=df.loc[df['dit']==True,['Chainage']]
        y=df.loc[df['dit_marker']==True,['Chainage']]
        plt.plot(z['Chainage'],[4]*len(z),'o',color='yellow',label="DIT",alpha=0.7,markersize=5)
        plt.plot(y['Chainage'],[4]*len(y),'|',color='yellow',markersize=20,alpha=0.3)


        z=df.loc[df['blow']==True,['Chainage']]
        y=df.loc[df['blow_marker']==True,['Chainage']]
        plt.plot(z['Chainage'],[5]*len(z),'o',color='orange',label="BLOWING",alpha=0.7,markersize=5)
        plt.plot(y['Chainage'],[5]*len(y),'|',color='orange',markersize=20,alpha=0.3)

        #labels = [item.get_text() for item in ax.get_yticklabels()]
        #labels[1] = 'HDD/OT/DRT'
        #labels[5] = 'DIT'
        #labels[7] = 'BLOWING'

        #ax.set_yticklabels(labels)



        plt.legend(loc="upper left")
        plt.title(spanid)

        
        #df.plot(kind='scatter',x=z,y=[2]*len(z),color='red')
        plt.show()