import pandas as pd

df = pd.read_csv('csv')
df2 = pd.read_csv('csv')




# df2 = pd.read_csv('temp_li_2.csv')
#
df2['EXPERTISE (subj matter)'] = 'NAVY'
#
# new_df = pd.merge(df2, df3, how='inner',  left_on=['First Name', 'Last Name'], right_on=['First Name', 'Last Name'])
# # df.combine_first(df2)
#
# # for i, row in df.iterrows():
# #     if row['First Name'] == df2['First Name'] and df['Last Name'] == df2['Last Name']:
# #         df.at[i, 'EXPERTISE (subj matter)'] = 'NAVY'
#
df_new = pd.concat([df, df2]).drop_duplicates(['First Name','Last Name', 'Experience', 'About'],keep='last').sort_values('First Name')
#
# print(df_new)
df_new.to_csv('temp merge.csv')




