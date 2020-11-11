import pandas as pd

df = pd.read_csv('csv')
df2 = pd.read_csv('csv')
df3 = pd.read_csv('csv')
df4 = pd.read_csv('csv')

df2['MARKET (agency/dept/client)'] = 'USAF'
df3['MARKET (agency/dept/client)'] = 'ARMY'
df4['MARKET (agency/dept/client)'] = 'NAVY'

df2[['First Name', 'Last Name']] = df2['Name'].str.split(' ', expand=True, n=1)
df2.drop('Name', axis=1, inplace=True)
df2['Last Name'] = df2['Last Name'].str.split(',').str[0]
df2['Last Name'] = df2['Last Name'].str.split(' ').str[0]

df3[['First Name', 'Last Name']] = df3['Name'].str.split(' ', expand=True, n=1)
df3.drop('Name', axis=1, inplace=True)
df3['Last Name'] = df3['Last Name'].str.split(',').str[0]
df3['Last Name'] = df3['Last Name'].str.split(' ').str[0]

df4[['First Name', 'Last Name']] = df4['Name'].str.split(' ', expand=True, n=1)
df4.drop('Name', axis=1, inplace=True)
df4['Last Name'] = df4['Last Name'].str.split(',').str[0]
df4['Last Name'] = df4['Last Name'].str.split(' ').str[0]

df_new = pd.concat([df, df2, df3, df4]).drop_duplicates(['First Name','Last Name', 'Experience', 'Description/Bio'],keep='last').sort_values('First Name')
df_new = pd.concat([df, df2, df3, df4]).sort_values('First Name')
#
# print(df_new)
df_new.to_csv('temp_leidos.csv')













# new_df = pd.merge(df, df2, how='inner', on=['First Name', 'Last Name'])
# # new_df = pd.concat([df,df2], axis=0)
# new_df.to_csv('NW_trial2.csv')
# df = pd.read_csv('NW_trial.csv')
#
# # df.groupby(['First Name','Last Name'])
# df.groupby(['First Name', 'Last Name']).agg('sum')
#
# df.to_csv('Testing again.csv')









# df = pd.read_csv('./csv\'s/BAH_PEOPLE_MASTER_NEW.csv')
# df2 = pd.read_csv('./csv\'s/BAH_NW.csv')
#
# df2.columns = ['First Name', 'Last Name', 'Title', 'Location']
#
# new_df = pd.merge(df, df2, how='inner', on=['First Name', 'Last Name'])
# # new_df = pd.concat([df,df2], axis=0)
# new_df.to_csv('NW_trial2.csv')
# # df = pd.read_csv('NW_trial.csv')
# #
# # # df.groupby(['First Name','Last Name'])
# # df.groupby(['First Name', 'Last Name']).agg('sum')
# #
# # df.to_csv('Testing again.csv')