from . import Generation_DataFrame as gd
import numpy as np


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
