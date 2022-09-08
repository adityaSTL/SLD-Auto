import pandas as pd
import numpy as np
from reading_spans import get_span as gs
import matplotlib.pyplot as plt
import seaborn as sns

class Master:

    def get_master(path,spanid):

        mylist=list(range(-200,20001))
        master=pd.DataFrame(mylist)
        df_tnd,df_hdd,df_drt,df_dit,df_blow=gs.get_df(path)
        all_df=[df_tnd,df_hdd,df_drt,df_dit,df_blow]

        df_all_span=gs.spanify(all_df,spanid)

        master['tnd_ot']=False
        master['tnd_ot_marker']=False
        master['tnd_hdd']=False
        master['tnd_hdd_marker']=False
        for i in range(len(df_all_span[0])):
            if df_all_span[0]['Method_Execution'][i]=='OT':
                master['tnd_ot']=master['tnd_ot']+master[0].between(int(df_all_span[0]['Chainage_From'][i]),int(df_all_span[0]['Chainage_To'][i]),inclusive="both")
                master['tnd_ot_marker']=master['tnd_ot_marker']+master[0].between(int(df_all_span[0]['Chainage_From'][i]),int(df_all_span[0]['Chainage_From'][i]),inclusive="both")
                master['tnd_ot_marker']=master['tnd_ot_marker']+master[0].between(int(df_all_span[0]['Chainage_To'][i]),int(df_all_span[0]['Chainage_To'][i]),inclusive="both")

            elif (df_all_span[0]['Method_Execution'][i]=='HDD'):
                master['tnd_hdd']=master['tnd_hdd']+master[0].between(int(df_all_span[0]['Chainage_From'][i]),int(df_all_span[0]['Chainage_To'][i]),inclusive="both")
                master['tnd_hdd_marker']=master['tnd_hdd_marker']+master[0].between(int(df_all_span[0]['Chainage_From'][i]),int(df_all_span[0]['Chainage_From'][i]),inclusive="both")
                master['tnd_hdd_marker']=master['tnd_hdd_marker']+master[0].between(int(df_all_span[0]['Chainage_To'][i]),int(df_all_span[0]['Chainage_To'][i]),inclusive="both")
        
        master['hdd']=False
        master['hdd_marker']=False
        for i in range(len(df_all_span[1])):
            master['hdd']=master['hdd']+master[0].between(int(df_all_span[1]['Chainage_From'][i]),int(df_all_span[1]['Chainage_To'][i]),inclusive="both")
            master['hdd_marker']=master['hdd_marker']+master[0].between(int(df_all_span[1]['Chainage_From'][i]),int(df_all_span[1]['Chainage_From'][i]),inclusive="both")
            master['hdd_marker']=master['hdd_marker']+master[0].between(int(df_all_span[1]['Chainage_To'][i]),int(df_all_span[1]['Chainage_To'][i]),inclusive="both")
        
        master['drt']=False
        master['drt_marker']=False
        master['drt_duct_dam']=False
        master['drt_duct_dam_marker']=False
        for i in range(len(df_all_span[2])):
            master['drt']=master['drt']+master[0].between(int(df_all_span[2]['Chainage_From'][i]),int(df_all_span[2]['Chainage_To'][i]),inclusive="both")
            master['drt_marker']=master['drt_marker']+master[0].between(int(df_all_span[2]['Chainage_From'][i]),int(df_all_span[2]['Chainage_From'][i]),inclusive="both")
            master['drt_marker']=master['drt_marker']+master[0].between(int(df_all_span[2]['Chainage_To'][i]),int(df_all_span[2]['Chainage_To'][i]),inclusive="both")
            if type(df_all_span[2]['Duct_dam_punct_loc_ch_from'][i])==int:
                master['drt_duct_dam']=master['drt_duct_dam']+master[0].between(int(df_all_span[2]['Duct_dam_punct_loc_ch_from'][i]),int(df_all_span[2]['Duct_dam_punct_loc_ch_to'][i]),inclusive="both")
                master['drt_duct_dam_marker']=master['drt_duct_dam_marker']+master[0].between(int(df_all_span[2]['Duct_dam_punct_loc_ch_from'][i]),int(df_all_span[2]['Duct_dam_punct_loc_ch_from'][i]),inclusive="both")
                master['drt_duct_dam_marker']=master['drt_duct_dam_marker']+master[0].between(int(df_all_span[2]['Duct_dam_punct_loc_ch_to'][i]),int(df_all_span[2]['Duct_dam_punct_loc_ch_to'][i]),inclusive="both")


        master['dit']=False
        master['dit_marker']=False
        master['dit_duct_miss']=False
        master['dit_duct_miss_marker']=False
        for i in range(len(df_all_span[3])):
            master['dit']=master['dit']+master[0].between(int(df_all_span[3]['Chainage_From'][i]),int(df_all_span[3]['Chainage_To'][i]),inclusive="both")
            master['dit_marker']=master['dit_marker']+master[0].between(int(df_all_span[3]['Chainage_From'][i]),int(df_all_span[3]['Chainage_From'][i]),inclusive="both")
            master['dit_marker']=master['dit_marker']+master[0].between(int(df_all_span[3]['Chainage_To'][i]),int(df_all_span[3]['Chainage_To'][i]),inclusive="both")    

            if type(df_all_span[3]['mb_duct_missing_sec_from'][i])==int:
                master['dit_duct_miss']=master['dit_duct_miss']+master[0].between(int(df_all_span[3]['mb_duct_missing_sec_from'][i]),int(df_all_span[3]['mb_duct_missing_sec_to'][i]),inclusive="both")
                master['dit_duct_miss_marker']=master['dit_duct_miss_marker']+master[0].between(int(df_all_span[3]['mb_duct_missing_sec_from'][i]),int(df_all_span[3]['mb_duct_missing_sec_from'][i]),inclusive="both")
                master['dit_duct_miss_marker']=master['dit_duct_miss_marker']+master[0].between(int(df_all_span[3]['mb_duct_missing_sec_to'][i]),int(df_all_span[3]['mb_duct_missing_sec_to'][i]),inclusive="both")    


        master['blow']=False
        master['blow_marker']=False
        for i in range(len(df_all_span[4])):
            master['blow']=master['blow']+master[0].between(int(df_all_span[4]['Chainage_From'][i]),int(df_all_span[4]['Chainage_To'][i]),inclusive="both")
            master['blow_marker']=master['blow_marker']+master[0].between(int(df_all_span[4]['Chainage_From'][i]),int(df_all_span[4]['Chainage_From'][i]),inclusive="both")
            master['blow_marker']=master['blow_marker']+master[0].between(int(df_all_span[4]['Chainage_To'][i]),int(df_all_span[4]['Chainage_To'][i]),inclusive="both")    


        #print(master.info())
        master.rename(columns = {0:'Chainage'}, inplace = True)
        master['duct_overlap']=False
        for i in range(len(master)):
            if master['drt_duct_dam'][i]*master['dit_duct_miss'][i]==True:
                master['duct_overlap'][i]=True

        master['tnd_overlap']=False
        for i in range(len(master)):
            if master['hdd'][i]*master['tnd_ot'][i]==True:
                master['tnd_overlap'][i]=True

        return master


        # loading data-set
        #iris = sns.load_dataset(master)
        # plotting strip plot with seaborn
        # deciding the attributes of dataset on
        # which plot should be made
        #ax = sns.swarmplot(x=master['hdd'], y=master[0])
