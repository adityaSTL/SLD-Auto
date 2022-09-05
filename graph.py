import pandas as pd
import numpy as np
from reading_spans import get_span as gs
import matplotlib.pyplot as plt
import seaborn as sns
from fine import Master as gm
from summ import summary

class plot:
    def get_plot(df):
        z=df.loc[df['blow']==True,'Chainage']
        print(z)
        
        #df.plot(kind='scatter',x=z,y=[2]*len(z),color='red')
        #plt.show()