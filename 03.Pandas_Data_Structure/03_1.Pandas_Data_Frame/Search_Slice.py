from . import Generation_DataFrame as gd
import numpy as np
import pandas as pd

df = pd.DataFrame(
    [[1, 2, 3, 4],
     [5, 6, 7, 8]],
    index=list('ab'),
    columns=list('abcd')
)

np.may_share_memory(gd.dfv, gd.df)
gd.dfv['b'] = 100
print(gd.dfv)
print(gd.df)

# Available to search all of data that includes
# Column's and Row's data.
print(gd.df.iloc[0])

# Set One-Row and One-Columns.
print(gd.df.iloc[0, 0])

s = gd.df.iloc[:, 0]
print(s)

# Slice results inquired by indexer
# also provide View.
np.may_share_memory(s, df)

