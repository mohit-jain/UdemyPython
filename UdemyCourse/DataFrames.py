'''
Created on Oct 3, 2017

@author: mohit.j
'''

import numpy as np
import pandas as pd

data = np.array([['', 'Col1', 'Col2'],
                 ['Row1', 1, 2],
                 ['Row2', 3, 4]
                ])

df = pd.DataFrame(data=data[1:,1:], index=data[1:,0], columns=data[0,1:])
print(df)

# Print height of the data frames
#print(df[0].count())

my_2darray = np.array([[1,2,3,4], [1,2,3,4]])
df = pd.DataFrame(data=my_2darray, index=range(0,2), columns=['A', 'B', 'C', 'D'])

print(df)
print(df.get_value(1, 'C', takeable=False))

# DataFrame from non dimensional array
data = {'Name':['Tom', 'Jack', 'Steve'], 'Age':[20,10,30]}
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)

# DataFrames from dictionary
data = [{'a' : 1, 'b' : 2}, {'a' : 2, 'b' : 3, 'c': 4}]
df = pd.DataFrame(data)
print(df) 

#With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])

#With two column indices with one index with other name
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print(df1)
print(df2)

# Creating DataFrame from dictionary of series
d = {'one' : pd.Series([1,2,3], index=['a', 'b', 'c']),
     'two' : pd.Series([1,2,3,4], index=['a', 'b', 'c','d'])
    }

df = pd.DataFrame(d)
print(df)

# Select only 1 column
print(df['one'])

# Addition of new columns by passing to a series
df['three'] = pd.Series([10,20,30], index=['a', 'b', 'c'])
print(df)

# Addition of the new column from the existing column
df['four'] = df['one'] + df['three']

print(df) 

# Deleting the column
del df['one']
print(df)

# Selection of row by label
print(df.loc['b'])

# Selection by integer location
print(df.iloc[2])
 
# Slicing of rows
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
    'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)
print(df[2:4])

# Addition of rows
df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2)
print(df) # index will get duplicated

# Deletion of rows
df = df.drop(0)
print(df)

