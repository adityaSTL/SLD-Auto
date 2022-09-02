import pandas as pd
import numpy as np
from reading_spans import get_span as gs

def filler(df,name,start,end):
    df[name]=df[0].between(start,end,inclusive="both")
    return df

def spanify(all_df,spanid):
    for i in range(len(all_df)):
        all_df[i]=all_df[i].loc[all_df[i]['Span_ID']==spanid]
        all_df[i].reset_index(inplace = True)
    return all_df

spanid=r"ADL-ASI-4635-M-01-GR01-03"
mylist=list(range(-200,20001))
master=pd.DataFrame(mylist)
#print(master)
path=r"data.db"
df_tnd,df_hdd,df_drt,df_dit,df_blow=gs.get_df(path)
all_df=[df_tnd,df_hdd,df_drt,df_dit,df_blow]

df_all_span=spanify(all_df,spanid)
#print(df[2])

for j in range(len(df_all_span)):
    for i in range(len(df_all_span[j])):
        master[j]=master[0].between(int(df_all_span[j]['Chainage_From'][i]),int(df_all_span[j]['Chainage_From'][i]))
print(master)

master.to_csv("master.csv")
#print(df_hdd_span)
print(master.info())

