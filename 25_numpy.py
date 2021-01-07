"Write a Program to show the utility of numpy and series  in python"
import pandas 
import numpy

data = numpy.array(['a', 'b', 'c', 'd'])

series = pandas.Series(data)
print(series)

series_inc_index = pandas.Series(data, index=[100, 101, 102, 103])
print(series_inc_index)
