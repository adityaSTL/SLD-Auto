import pandas as pd
import numpy as np
from reading_spans import get_span as gs

def filler(master,df,mb):
    master[mb]=False
    for i in range(len(df)):
        master[mb]=master[mb]+master[0].between(int(df['Chainage_From'][i]),int(df['Chainage_From'][i]),inclusive="both")
    return master

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



master=filler(master,df_all_span[0],"tnd")
master=filler(master,df_all_span[1],"hdd")
master=filler(master,df_all_span[2],"drt")
master=filler(master,df_all_span[3],"dit")
master=filler(master,df_all_span[4],"blow")

master.to_csv("master1.csv")
#print(df_hdd_span)
print(master.info())

