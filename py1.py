import numpy as np
import asciitable as ac
import pandas as pd

# Open a file: file
#file = open('datas\clicking_data', 'r')

#actbl = ac.read('datas\clicking_data')

# Get a Reader object
#table = ac.get_reader(Reader=ac.BasicReader)

# Read a table from a file
#data = table.read('datas\clicking_data')

# Write the data in a variety of ways using higher-level Reader object.

#ac.write(table, Writer=ac.CommentedHeader )
#ac.write(table, Writer=ac.BasicReader )
#ac.write(table, Writer=ac.Rdb, exclude_names=['CHI'] )

filename = 'datas\clicking_data'
#names = ['action', 'action_label', 'action_type', 'tstamp', 'user_session']
data = pd.read_csv(filename, header=0, sep="\t")
#print(data.shape)

#print complete matrix / dataset
#print(data)

#data.iloc[<row selection>, <column selection>]
#see examples below

print("data.iloc row 0 & 1, column 0 & 1")
print(data.iloc[0:2, 0:2])

print("")

print("data.iloc row 0, column 0 & 1")
print(data.iloc[0:1, 0:2])

print("")

print("data.iloc row 0, column 0, 1 & 2")
print(data.iloc[0:1, 0:3])

print("")

print("data.iloc row 0, column 1 & 2")
print(data.iloc[0:1, 1:3])

# Print it
#print(file.read())

#print(actbl)

# Check whether file is closed
#print(file.closed)

# Close file
#file.close()

# Check whether file is closed
#print(file.closed)
