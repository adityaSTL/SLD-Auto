# SLD-Auto
Use to create pictorial representation of span based on different parameters (OT,HDD,DRT,DIT,Blowing)
/nAditya is making changes in this branch, once completed this can be pushed to main


Reading spans list of functions:
1. spanify    : Use to get mb reports of only selected span
2. check_span : Use to check if particular mb report has data corresponding to selected span
3. get_df     : Use to extract the pandas df from data.db file
4. df_info    : Use to get .info() of extracted dataframes

5. get_master : Use to get mixed mb report from all mb reports (unprocessed)

6. get_stats  : Use to get processed final dataframe and other stats of the span

7. get_plot   : Use to plot graph from dataframe