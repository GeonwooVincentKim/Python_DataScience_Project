import pandas as pd
import numpy as np

# Label of 'rows' includes 'index parameter'.
# Label of 'columns' includes 'columns parameter'.
df = pd.DataFrame(
    [[1, 2, 3, 4],
     [5, 6, 7, 8]],
    index=list('ab'),
    columns=list('abcd')
)

print(df)
print(df.values)
type(df.values)

print(df.index)
print(df.columns)

print(df.shape, df.ndim, df.size)

# The difference between Series
# and index operation is treated by heat.
try:
    print(df[0])

except Exception as e:
    print(e)

print(df['a'])
print(df.loc['a'])  # Search rows based on 'loc' indexer.
print(df.loc['a', :])

print(df.loc['a':, 'b': 'c'])

dfv = df.loc['a':, 'b': 'c']


np.may_share_memory(dfv, df)
dfv['b'] = 100
print(dfv)
print(df)

# Available to search all of data that includes
# Column's and Row's data.
print(df.iloc[0])

# Set One-Row and One-Columns.
print(df.iloc[0, 0])

s = df.iloc[:, 0]
print(s)

# Slice results inquired by indexer
# also provide View.
print(np.may_share_memory(s, df))

# Allocate to the variable, 'df_'/
data = [[1, 3], [4, 5]]
columns = ['A', 'B']
df_ = pd.DataFrame(data=data, columns=columns)

# Check the data-format of Dataframe
# as 'dtype' attribute.
print(df_.dtypes)

# Set Column of 'A' as 'str',
# and then set other Colunm of 'B' as 'np.int32'.
df_c = df_.astype({'A': str, 'B': np.int32})

