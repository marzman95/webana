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

print("clicking_data.iloc row 0 until 5, column 0 & 1")
print(c_data.iloc[0:5, 0:2])

print("")

print("clicking_data.iloc row 0 until 5, column 1 & 2")
print(c_data.iloc[0:5, 1:3])

print("")

print("clicking_data.iloc row 0 until 5, column 0, 3 & 4")
print(c_data.iloc[0:5, [0,3,4]])

print("")

print("meta_data.iloc row 0 until 5, column 0 & 1")
print(m_data.iloc[0:5, 0:2])

print("")

print("meta_data.iloc row 0 until 5, column 1 & 2")
print(m_data.iloc[0:5, 1:3])

print("")

print("meta_data.iloc row 0 until 5, all columns") #doesn't fit :-(
print(m_data.iloc[0:5, :])

print("")

print("experiment_details_5.iloc row 0 until 5, column 0 & 1")
print(e_data.iloc[0:5, 0:2])

print("")

print("experiment_details_5.iloc row 0 until 5, column 0, 1 & 2")
print(e_data.iloc[0:5, 0:3])

print("")

print("experiment_details_5.iloc row 0 until 5, column 0, 2 & 3")
print(e_data.iloc[0:5, [0,2,3]])

print("")

#select data based on conditions
clic = c_data['action'] == "clic"
view = c_data['action'] == "view"

print("clicking_data[clic] & column action, tstamp, u_session & no duplicates")
sel = c_data[clic]
sel.drop_duplicates()
print(sel.iloc[:, [0,3,4]])

# Print it
#print(file.read())

#print(actbl)

# Check whether file is closed
#print(file.closed)

# Close file
#file.close()

# Check whether file is closed
#print(file.closed)
