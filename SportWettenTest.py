
import csv
import pandas as pd
import numpy as np

import openpyxl

file_name='sportwettentest.csv'
writer = pd.ExcelWriter('Results.xlsx', engine='openpyxl', header = True, index=False)
sw_data = pd.DataFrame()

sw_data=pd.read_csv(filepath_or_buffer = file_name, sep = ",", header = 1)

#Question 1
#Check if any columns with string contains 'interwetten-news'
interwetten=None

for cols in sw_data.columns:
    if sw_data[cols].dtype=='O':
        if sw_data[cols].str.contains('interwetten-news').any():
            if interwetten is None:
                interwetten = sw_data.loc[(sw_data[cols].dropna().str.contains('interwetten-news')) & (sw_data['Response Time']<=0.5) & (sw_data['Content'].str.contains('html'))]
            else:
                interwetten.append(sw_data.loc[(sw_data[cols].str.contains('interwetten-news')) & (sw_data[cols].notnull()) & (sw_data['Response Time']<=0.5) & (sw_data['Content'].str.contains('html'))])


#Write answer to file
interwetten['Address'].to_excel(writer, sheet_name='Question_1', index=False)
writer.close()

#Question 2.

#I can see that there is no status code 302, Moved Temporarily: 
# print(sw_data['Status Code'].dropna().unique())


#Also only the following status values:
#['OK' 'Blocked by robots.txt' 'Moved Permanently' 'Not Found']
# print(sw_data['Status'].dropna().unique())

#Looked for text 'plus.google.com', also no matches

interwetten2=None
for cols in sw_data.columns:
    if sw_data[cols].dtype=='O':
        if sw_data[cols].str.contains('google').any():
            print(cols)
            if interwetten2 is None:
                interwetten2 = sw_data.loc[sw_data[cols].str.contains('plus.google.com') & sw_data[cols].notnull() & (sw_data['Content'].str.contains('html')) & (sw_data['Inlinks']>1) ]
            else:
                interwetten2.append(sw_data.loc[sw_data[cols].str.contains('plus.google.com') & sw_data[cols].notnull() &  (sw_data['Content'].str.contains('html')) & (sw_data['Inlinks']>1) ] )


interwetten2.to_excel(writer, sheet_name='Question_2', index=False)
writer.close()

# #Question 3

interwetten3 = pd.DataFrame()

interwetten3 = sw_data[(sw_data['Title 1 Length'].dropna() > 65) & (sw_data['Title 1'].str.contains('2018')) & ((sw_data['Title 1 Pixel Width'] < 550) | (sw_data['Title 1 Pixel Width'] > 700)) ]

interwetten3['Title 1'].to_excel(writer, sheet_name='Question_3', index=False)
writer.close()


