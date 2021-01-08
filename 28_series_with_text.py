"Write a Program to use series with text file"
import pandas

content = []
with open('28_read_file.txt') as file:
    for line in file:
        for word in line.split():
            content.append(word)

series = pandas.Series(content)
print(series)
        



__OUTPUT__ = """
0      Line
1        01
2         *
3      Line
4        02
5        **
6      Line
7        03
8       ***
9      Line
10       04
11     ****
12     Line
13       05
14    *****
dtype: object
"""