'''
Created on Oct 9, 2017

@author: mohit.j
'''

import pandas as pd
import numpy as np

# Pandas Data structures
# 1. Series
# Homogeneous, Size Immutable, value Mutable

# create empty series
s = pd.Series()

# create a series from ndarray
data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data)
print(s)

# create series from array with index.
s = pd.Series(data, index=[100,101,102,103])
print(s)

# create the series from dictionary
data = {'a':1., 'b':2., 'c':3.}
s = pd.Series(data)

# dictionary keys are used to construct index. change the order using the index
s = pd.Series(data, index=['b', 'a', 'c'])
print(s)

# using label. if not not found than exception will raised
print(s['a'])
# multiple elements using list of labels
print(s[['a','b', 'c']])

# Create the series from scalar
s = pd.Series(5, index=[0,1,2,3])
print(s)

# Retreiving the data from series
print(s[0])
# Retreive the first 3 element from series
print(s[:3])
# last 3 element
print(s[-3:])

#2. DataFrames
# DataFrame from list
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)

data = [['Alex',10], ['Bob', 12], ['Clarke', 30]]
df = pd.DataFrame(data, columns=['Name', 'Age'], dtype = float)
print(df)

# Datafrmaes from dict
data = {'Name' : ['Tom', 'Jack', 'Steve'], 'Age': [23,21,34]}
df = pd.DataFrame(data)
print(df)

# provide index to rows
df = pd.DataFrame(data, index=['r1', 'r2', 'r3'])
print(df)

# Creating Data Frame from List of Dictionaries
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=["r1", "r2"])
print(df)

Contentlist = ['Audit.AzureActiveDirectory', 'Audit.Exchange']
print(Contentlist)
Contentlist.remove('Audit.Exchange')
print(Contentlist)


if __name__ == '__main__':
    pass