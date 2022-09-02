import sqlite3
import pandas as pd
import matplotlib

import matplotlib.pyplot as plt
import seaborn as sns

class get_span:


    ###########################################################################################################################
    def check_span(spanid,all_df):
        df=0
        for j in range(len(all_df)):
            count=0
            for i in range(len(all_df[j])):
                if (all_df[j]['Span_ID'][i]==spanid):
                    count+=1
            if count==0:
                print("No span id matching in "+str(df))
            df+=1       
    ###########################################################################################################################             
    def df_info(all_df):
        for i in range(len(all_df)):
                print(all_df[i].info())
    ###########################################################################################################################
    def plot_span(y,df,spanid,method,color):
        if 1:
            xmin=df['Chainage_From'][0]
            #print("1")
            for i in range(len(df)):
                if (df['Span_ID'][i]==spanid):
                    plt.hlines(y,df['Chainage_From'][i],df['Chainage_To'][i],color=color,linewidth=7)
                    xmin=min(xmin,df['Chainage_From'][i])
            plt.text(xmin,y,method, ha='left', va='baseline',weight='bold')       
    ###########################################################################################################################
    def get_df(path):
        cnx = sqlite3.connect(path)
        df_tnd = pd.read_sql_query("SELECT * FROM 'tnd'", cnx)
        df_hdd = pd.read_sql_query("SELECT * FROM 'hdd'", cnx)
        df_drt = pd.read_sql_query("SELECT * FROM 'drt'", cnx)
        df_dit = pd.read_sql_query("SELECT * FROM 'dit'", cnx)
        df_blow = pd.read_sql_query("SELECT * FROM 'blowing'", cnx)
        return df_tnd,df_hdd,df_drt,df_dit,df_blow

    ###########################################################################################################################
