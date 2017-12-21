import numpy as np
import asciitable as ac

# Open a file: file
file = open('datas\clicking_data', 'r')

actbl = ac.read('datas\clicking_data')

# Get a Reader object
table = ac.get_reader(Reader=ac.BasicReader)

# Read a table from a file.  Return a NumPy record array object and also
# update column and metadata attributes in the "table" Reader object.
data = table.read('datas\clicking_data')

# Write the data in a variety of ways using as input both the NumPy record
# array and the higher-level Reader object.

#ac.write(table, Writer=ac.CommentedHeader )
ac.write(table, Writer=ac.BasicReader )
#ac.write(table, Writer=ac.Rdb, exclude_names=['CHI'] )

# Print it
#print(file.read())

#print(actbl)

# Check whether file is closed
#print(file.closed)

# Close file
#file.close()

# Check whether file is closed
#print(file.closed)
