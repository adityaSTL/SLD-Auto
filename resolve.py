import sqlite3
import pandas as pd
import matplotlib
from reading_spans import get_span as gs
import matplotlib.pyplot as plt
import seaborn as sns

path=r"C:\Users\Aditya.gupta\Downloads\data.db"
df_tnd,df_hdd,df_drt,df_dit,df_blow=gs.get_df(path)
all_df=[df_tnd,df_hdd,df_drt,df_dit,df_blow]


df_drt.info()
cnx = sqlite3.connect(path)
#cnx.execute("ALTER TABLE 'drt' RENAME COLUMN 'ch_from' TO 'Chainage_From' ")
#cnx.execute("ALTER TABLE 'drt' RENAME COLUMN 'ch_to' TO 'Chainage_To' ")
df_drt.info()