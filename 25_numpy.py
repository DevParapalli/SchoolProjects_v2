"Write a Program to show the utility of numpy and series  in python"
import pandas 
import numpy

data = numpy.array(['a', 'b', 'c', 'd'])

series = pandas.Series(data)
print(series)

series_inc_index = pandas.Series(data, index=[100, 101, 102, 103])
print(series_inc_index)


__OUTPUT__ = """
0    a
1    b
2    c
3    d
dtype: object
100    a
101    b
102    c
103    d
dtype: object
"""