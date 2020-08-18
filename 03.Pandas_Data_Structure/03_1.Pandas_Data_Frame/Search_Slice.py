from .Generation_DataFrame import *
import numpy as np


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
