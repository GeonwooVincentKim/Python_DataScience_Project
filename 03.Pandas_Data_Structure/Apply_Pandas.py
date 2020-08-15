import pandas as pd
s = pd.Series([1, 2, 3, 4], index=list('abcd'))
print(s)

print(s.values)
print(s.index)
print("s.shape : {0}, number of dimension of variable 's' : {1}, s.size : {2}".format(
    s.shape, s.ndim, s.size
))

# Available search Label.
print(s[0], s['a'])
print(s[0:2])
