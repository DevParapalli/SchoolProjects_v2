"Write a Program to read CSV file and show its data in python using dataFrames and pandas."

import pandas
data_frame = pandas.read_csv('36_read_csv.csv', nrows=12)

# Display Rows
print(data_frame)

#Shape of CSV
print(f"Format: {data_frame.shape}")

#Columns
print(f"Columns: {data_frame.columns}")

