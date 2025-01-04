import pandas as pd

'''
Series is used to model one dimensional data, similar to a list.
Series object has an index and a name.

A common idea through pandas is the notion of an axis.
Series is one dimensional so it has a single axis - the index.
'''

# Examples in pure python


def get(ser, idx):
    # Pull items from dict based on index
    value_idx = ser['index'].index(idx)
    return ser['data'][value_idx]

# simple example
ser = {'index': [0, 1, 2, 3],
       'data': [145, 142, 38, 13],
       'name': 'songs'}

item = get(ser, 1)
print("Get item from data set in index 1:", item)  # 142

# Using non-integer values for index
songs = {'index': ['Paul', 'John', 'George', 'Ringo'],
         'data': [145, 142, 38, 13],
         'name': 'counts'}

song_count = get(songs, 'John')
print("Get song count by John:", item)

# Using pandas Series

songs2 = pd.Series([145, 142, 38, 13], name='counts')
print(songs2)

'''
0    145
1    142
2     38
3     13
Name: counts, dtype: int64

Left most column is the index, or the axis and the values are called axis labels.
dtype is the type of the values.
'''

songs2_idx = songs2.index
print(songs2_idx)  # RangeIndex(start=0, stop=4, step=1)

songs3 = pd.Series([145, 142, 38, 13], 
                   name='counts',
                   index=['Paul', 'John', 'George', 'Ringo'])

songs3_idx = songs3.index
print(songs3_idx)  # Index(['Paul', 'John', 'George', 'Ringo'], dtype='object')


'''
Data for a series doesn't have to be homogeneous.
We can insert Python objects to a Series:
'''

class Foo:
    pass

ringo = pd.Series(['Richard', 'Starkey', 13, Foo()],
                  name = 'ringo')
print(ringo)

'''
0                                 Richard
1                                 Starkey
2                                      13
3    <__main__.Foo object at 0x11b749a90>
Name: ringo, dtype: object
'''

'''
Object data type is used for strings and values with heterogenous types.
Numeric data should be int64 or float64 to do vectorized numeric operations.
Time data should be datetime64[ns] for date operations.
'''
