import pandas as pd
import numpy as np
import os

df = pd.read_csv('csv')
df['Description/Bio2'] = df['Description/Bio'].astype(str) + df['About'].astype(str)
df.to_csv('merged_aabout.csv')

#
# df = pd.read_csv("'csv's/BAH_PEOPLE_MASTER (update).csv'")
# df2 = pd.read_csv('csv')
#
# # df = pd.read_csv('temp.csv')
# # df2 = pd.read_csv('temp_li.csv')
# #
# new_df = pd.merge(df, df2, how='outer',  left_on=['First Name', 'Last Name'], right_on=['First Name', 'Last Name'])
# print(new_df)
# new_df.to_csv('mergev2.csv')
# #
# #
# # df = pd.read_csv('mergev1.csv')
# # df2 = pd.read_csv('BAH PMs GW list of 94.csv')
#
#
#
#











# # df['trial f'] = df['First Name'].str.split('. ').str[-1]
# # df.drop('First Name', axis=1, inplace=True)
# df['temp'] = df['Last Name'].str.split(' ').str[0]
# # df.drop('Last Name', axis=1, inplace=True)
# df['LastName'] = df['temp'].str.split(',').str[0]
# df.drop('temp', axis=1, inplace=True)
# print(df)
# df.to_csv('testing.csv')


#
# pm_fname = df[df.columns[0]]
# pm_lname = df[df.columns[1]]
#
# pm_combo = df2[df2.columns[1]]
#
# df['Name'] = df['First Name'] + " " + df['Last Name']
# print(df['Name'])
# #
# df2[['First Name', 'Last Name']] = df2['Name'].str.split(' ', expand=True, n=1)
# df2.drop('Name', axis=1, inplace=True)
# df2['Last Name'] = df2['Last Name'].str.split(',').str[0]
# print(df2)
# df2.to_csv('temp_li.csv')
# #
# df['Last Name'] = df['Last Name'].str.split(',').str[0]
# df['Last Name'] = df['Last Name'].str.split(' ').str[0]
# temp = df[df['Last Name'].isnull()]
# temp.to_csv('fix.csv')
# print(temp)
# df.to_csv('temp.csv')


# #
# # df2.drop('Unnamed: 0', axis=1, inplace=True)
# # print(df2)
# #
# mergedStuff = pd.merge(df, df2, on=['Name'], how='inner')
# print(mergedStuff)
# mergedStuff.to_csv('temp.csv')
#
# # for name in pm_fname:
# #     print(name)
# #
# # print(pm_fname)