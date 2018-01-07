import numpy as np
import pandas as pd
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype

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

selm = m_data.iloc[:,[1,2,3,4,5,6,7,8,12,13,15,16,17,18,19,20,21,22,24,25,26,27,29]]

merge = pd.merge(selm, e_data, on='user_id', suffixes=('_s', '_e'))

merge3 = pd.merge(merge, c_data, left_on='user_id', right_on='user_session', suffixes=('_s', '_c'))

selt = merge3.iloc[:,[0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]]

for column in selt:
    if is_string_dtype(selt[column]):
        print(column, "is string")
    else:
        if is_numeric_dtype(selt[column]):
            print(column, "is numeric")
            print("min:", selt[column].min())
            print("max:", selt[column].max())
    print("")

Count_RowT = selt.shape[0] #gives number of row count
Count_ColT = selt.shape[1] #gives number of col count
print("selt has",Count_RowT, "rows &", Count_ColT, "columns")

#select data (subset) based on (a) condition(s)
clic = selt['action'] == "clic"
view = selt['action'] == "view"
con1 = selt['condition'] == "1-Control"
con2 = selt['condition'] == "2-Buttony-Conversion-Buttons"
dvc1 = selt['dvce_type'] == "Mobile"
dvc2 = selt['dvce_type'] != "Mobile"

sub = selt[clic & con1 & dvc1]

print("total_data & conditions")
print(sub)

# Delete comment of the next to lines to obtain the merged dataset as a CSV-file
#print("Exporting data")
#selt.to_csv("export.csv", sep=';')
