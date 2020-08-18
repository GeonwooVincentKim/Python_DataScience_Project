import pandas as pd

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
print(df.loc(['a']))
print(df.loc['a', :])
