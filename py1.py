import numpy as np
#import asciitable as ac
import pandas as pd

filename = 'datas\clicking_data'
c_data = pd.read_csv(filename, header=0, sep="\t") #clicking_data

filename2 = 'datas\meta_data'
m_data = pd.read_csv(filename2, header=0, sep="\t", encoding = "ISO-8859-1") #meta_data

filename3 = 'datas\experiment_details_5'
e_data = pd.read_csv(filename3, header=0) #experiment_details_5

Count_Row = c_data.shape[0] #gives number of row count
Count_Col = c_data.shape[1] #gives number of col count
print("clicking_data has",Count_Row, "rows &", Count_Col, "columns")

Count_Row2 = m_data.shape[0] #gives number of row count
Count_Col2 = m_data.shape[1] #gives number of col count
print("meta_data has",Count_Row2, "rows &", Count_Col2, "columns")

Count_Row3 = e_data.shape[0] #gives number of row count
Count_Col3 = e_data.shape[1] #gives number of col count
print("experiment_details_5 has",Count_Row3, "rows &", Count_Col3, "columns")

print("")

#print complete matrix / dataset of clicking_data
#print(c_data)

#print complete matrix / dataset of meta_data
#print(m_data)

#print complete matrix / dataset of experiment_details_5
#print(e_data)

#data.iloc[<row selection>, <column selection>]
#see examples below

'''
print("clicking_data.iloc row 0 until 5, column 0 & 1")
print(c_data.iloc[0:5, 0:2])

print("clicking_data.iloc row 0 until 5, column 0, 3 & 4")
print(c_data.iloc[0:5, [0,3,4]])

print("meta_data.iloc row 0 until 5, column 1 & 2")
print(m_data.iloc[0:5, 1:3])

print("meta_data.iloc row 0 until 5, all columns") #doesn't fit :-(
print(m_data.iloc[0:5, :])

print("experiment_details_5.iloc row 0 until 5, column 0, 1 & 2")
print(e_data.iloc[0:5, 0:3])

print("experiment_details_5.iloc row 0 until 5, column 0, 2 & 3")
print(e_data.iloc[0:5, [0,2,3]])
'''

selm = m_data.iloc[:,[1,2,3,4,5,6,7,8,12,13,15,16,17,18,19,20,21,22,24,25,26,27,29]]
'''
print("selm")
print(selm)
print(selm.iloc[:,[9,10,11]])
'''

merge = pd.merge(selm, e_data, on='user_id', suffixes=('_s', '_e'))
#merge2 = pd.merge(selm, c_data, left_on='user_id', right_on='user_session', suffixes=('_s', '_c'))
merge3 = pd.merge(merge, c_data, left_on='user_id', right_on='user_session', suffixes=('_s', '_c'))

#selt = merge3.iloc[:,0:30]
selt = merge3.iloc[:,[0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]]
#print(selt)
ndup = selt.drop_duplicates()

#select data (subset) based on (a) condition(s)
clic = selt['action'] == "clic"
view = selt['action'] == "view"
con1 = selt['condition'] == "1-Control"
con2 = selt['condition'] == "2-Buttony-Conversion-Buttons"
dvc1 = selt['dvce_type'] == "Mobile"
dvc2 = selt['dvce_type'] != "Mobile"

sub = selt[clic & con1 & dvc1]

#sub2 = ndup[clic & con1 & dvc1]
#warning will occur for ndup, doesn't affect result & performance but feels bad

print("total_data & conditions")
print(sub)

# Delete comment of the next to lines to obtain the merged dataset as a CSV-file
#print("Exporting data")
#selt.to_csv("export.csv", sep=';')

#print("no duplicates & conditions")
#print(sub2)

# Print it
#print(file.read())

#print(actbl)

# Check whether file is closed
#print(file.closed)

# Close file
#file.close()

# Check whether file is closed
#print(file.closed)
