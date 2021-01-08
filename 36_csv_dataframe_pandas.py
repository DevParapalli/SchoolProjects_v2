"Write a Program to read CSV file and show its data in python "
"using dataFrames and pandas."

import pandas
data_frame = pandas.read_csv('36_read_csv.csv', nrows=12)

# Display Rows
print(data_frame)

#Shape of CSV
print(f"Format: {data_frame.shape}")

#Columns
print(f"Columns: {data_frame.columns}")



__OUTPUT__ = """
       name   class   marks  remarks
0    dummy1      12     100    dummy
1    dummy2      12     100    dummy
2    dummy3      12     100    dummy
3    dummy4      12     100    dummy
4    dummy5      12     100    dummy
5    dummy6      12     100    dummy
6    dummy7      12     100    dummy
7    dummy8      12     100    dummy
8    dummy9      12     100    dummy
9   dummy10      12     100    dummy
10  dummy11      12     100    dummy
Format: (11, 4)
Columns: Index(['name', ' class', ' marks', ' remarks'], 
dtype='object')
"""