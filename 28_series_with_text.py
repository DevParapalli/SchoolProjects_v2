"Write a Program to use series with text file"
import pandas

content = []
with open('28_read_file.txt') as file:
    for line in file:
        for word in line.split():
            content.append(word)

series = pandas.Series(content)
print(series)
        

