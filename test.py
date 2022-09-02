import sqlite3
import pandas as pd
import matplotlib
from reading_spans import get_span as gs
import matplotlib.pyplot as plt
import seaborn as sns


path=r"data.db"
df_tnd,df_hdd,df_drt,df_dit,df_blow=gs.get_df(path)
all_df=[df_tnd,df_hdd,df_drt,df_dit,df_blow]
#df_info(all_df)
spanid="ADL-TAN-4680-M-01-GR01-02"
gs.check_span(spanid,all_df)

cnx = sqlite3.connect(path)
#cnx.execute("ALTER TABLE 'drt' RENAME COLUMN 'ch_from' TO 'Chainage_From' ")
#cnx.execute("ALTER TABLE 'drt' RENAME COLUMN 'ch_to' TO 'Chainage_To' ")
#df_drt.info()
#sns.despine()

#print(df_tnd.loc[df_tnd['Span_ID']==spanid,['Chainage_From','Chainage_To']])
len=len(df_tnd.loc[df_tnd['Span_ID']==spanid,['Chainage_From','Chainage_To']])
#plt.xlim(-20, 3000)
mandal=str(df_blow.loc[df_blow['Span_ID']==spanid,'Mandal_Name'])
district=str(df_blow.loc[df_blow['Span_ID']==spanid,'District_Name'])
plt.title(spanid)
#plt.text(0.5, 0.5, "Mandal:"+mandal, fontsize=12)
gs.plot_span(11,df_tnd,spanid,"T&D","blue")
gs.plot_span(9,df_hdd,spanid,"HDD","green")
gs.plot_span(7,df_drt,spanid,"DRT","red")
gs.plot_span(5,df_dit,spanid,"DIT","yellow")
gs.plot_span(3,df_blow,spanid,"BLO","orange")
#plt.axis([-50, 5, 1, 12])
plt.yticks([]) 
plt.xticks(rotation=90)
plt.show()
            
#print(count1,count2,count3,count4,count5)
#plt.axes.get_yaxis().set_visible(False)