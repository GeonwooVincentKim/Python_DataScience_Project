import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3, 4], index=list('abcd'))
print(s)

# Check 'value' attribute of series.
print(s.values)
print(s.index)
print("s.shape : {0}, number of dimension of variable 's' : {1}, s.size : {2}".format(
    s.shape, s.ndim, s.size
))

# Available search Label.
print(s[0], s['a'])
print(s[0:2])
print(s['a': 'c'])

# Allocate to the variable by search slide.
sv = s['a': 'c']


np.may_share_memory(sv, s)
print(sv)

sv['a'] = 999
print(sv)
print(s)

s['e'] = 100
print(s)

try:
    # Add Index-Operation to integer.
    s[5] = 300
except Exception as e:
    print(e)
