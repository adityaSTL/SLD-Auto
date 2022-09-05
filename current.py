import pandas as pd
import numpy as np
from reading_spans import get_span as gs
import matplotlib.pyplot as plt
import seaborn as sns
from fine import Master as gm
from summ import summary
from graph import plot

path=r'data.db'
spanid="ADL-WAN-4685-M-01-GR03-01"

df=gm.get_master(path,spanid)
(df_summ,all_stats)=summary.get_stats(df)

plot.get_plot(spanid,df_summ)
plt.title(spanid)
df_summ.to_csv("final.csv")
#z=(df_summ.loc[df['blow']==True,['Chainage']])
#df_summ.plot(kind='scatter',x=z,y=[2]*len(z),color='red')
#plt.show()
#print(df_summ.info())
#print(all_stats)
