# %%
from IPython import get_ipython

# %%
import numpy as np
import pandas as pd

# %%
df = pd.DataFrame([[1, 1.2, np.nan],
                   [2.4, 5.5, 4.2],
                   [np.nan, np.nan, np.nan],
                   [0.44, -3.1, -4.1]],
                  index=[1, 2, 3, 4],
                  columns=['A', 'B', 'C'])
df

# %%
df.head(2)

# %%
df.tail(2)

# %%
df.describe()

# %%
print(df)
print(np.argmin(df), np.argmax(df))

# %%
print(df)
print(df.idxmin())
print(df.idxmax())

# %%
print(df)
print(df.std())
print(df.var())

# %%
print(df)
print(df.skew())
print(df.kurt())

# %%
print(df)
print(df.sum())
print(df.cumsum()) # 누적합

# %%
print(df)
print(df.prod())
print(df.cumprod())

# %%
df.diff() # 같은 컬럼 기준으로 아래행에서 위행을 뺀 값

# %%
df.quantile()

# %%
df.pct_change() # 같은 컬럼 기준으로 아래행에서 위행을 뺀 값을 위행으로 나눈다

# %%
df.corr()

# %%
df.corrwith(df.B) # 컬럼 B에 관한 상관관계 출력

# %%
df.cov() # 공분산

# %%
df['B'].unique()

# %%
df['A'].value_counts()


# %%
# Group by 연산


# %%
df = pd.DataFrame({'c1': ['a', 'a', 'b', 'b', 'c', 'd', 'b'],
                   'c2': ['A', 'B', 'B', 'A', 'D', 'C', 'C'],
                   'c3': np.random.randint(7),
                   'c4': np.random.random(7)})
df

# %%
df.dtypes

# %%
df['c3'].groupby(df['c1']).mean() # groupby에 들어가는 컬럼이 기준이된다.

# %%
df['c4'].groupby(df['c2']).std()

# %%
df['c4'].groupby([df['c1'], df['c2']]).mean()

# %%
df['c4'].groupby([df['c1'], df['c2']]).mean().unstack()

# %%
df.groupby('c1').mean()

# %%
df.groupby(['c1', 'c2']).mean()

# %%
df.groupby(['c1', 'c2']).size()

# %%
for c1, group in df.groupby('c1'):
  print(c1)
  print(group)
  
# %%
for (c1, c2), group in df.groupby(['c1', 'c2']):
  print((c1, c2))
  print(group)
  
# %%
df.groupby(['c1', 'c2'])[['c4']].mean()

# %%
df.groupby('c1')['c3'].quantile()

# %%
df.groupby('c1')['c3'].count()

# %%
df.groupby('c1')['c4'].median()

# %%
df.groupby('c1')['c4'].std()

# %%
df.groupby(['c1', 'c2'])['c4'].agg(['mean', 'min', 'max'])
# 여러 집계함수를 한꺼번에 사용할 때 .agg을 사용한다.

# %%
df.groupby(['c1', 'c2'], as_index=False)['c4'].mean()
# 기준이 되는 'c1'과 'c2'를 index가 아닌 컬럼으로 만들어 출력한다.

# %%
df.groupby(['c1', 'c2'], group_keys=False)['c4'].mean()
# 그룹지정이 아닌 따로따로 출력

# %%
def top(df, n=3, column='c1'):
  return df.sort_values(by=column)[-n:]

top(df, n=5)

# %%
df.groupby('c1').apply(top)


# %%
# 피벗 테이블 (Pivot Table)


# %%
df.pivot_table(['c3', 'c4'],
               index=['c1'],
               columns=['c2'])

# %%
df.pivot_table(['c3', 'c4'],
               index=['c1'],
               columns=['c2'],
               margins=True)

# %%
df.pivot_table(['c3', 'c4'],
               index=['c1'],
               columns=['c2'],
               margins=True,
               aggfunc=sum)

# %%
df.pivot_table(['c3', 'c4'],
               index=['c1'],
               columns=['c2'],
               margins=True,
               aggfunc=sum,
               fill_value=0)

# %%
pd.crosstab(df.c1, df.c2)

# %%
pd.crosstab(df.c1, df.c2, values=df.c3, aggfunc=sum, margins=True)


# %%
# 범주형 (Categorical) 데이터


# %%
s = pd.Series(['c1', 'c2', 'c1', 'c2', 'c1']* 2)
s

# %%
pd.unique(s)

# %%
pd.value_counts(s)

# %%
code = pd.Series([0, 1, 0, 1, 0]* 2)
code

# %%
d = pd.Series(['c1', 'c2'])
d

# %%
d.take(code)

# %%
df = pd.DataFrame({'id': np.arange(len(s)),
                   'c': s,
                   'v': np.random.randint(1000, 5000, size=len(s))})
df

# %%
c = df['c'].astype('category')
c

# %%
c.values

# %%
c.values.categories

# %%
c.values.codes

# %%
df['c'] = c
df.c

# %%
c = pd.Categorical(['c1', 'c2', 'c3', 'c1', 'c2'])
c

# %%
categories = ['c1', 'c2', 'c3']
codes = [0, 1, 2, 0, 1]
c = pd.Categorical.from_codes(codes, categories)
c

# %%
pd.Categorical.from_codes(codes, categories, ordered=True)

# %%
c.as_ordered()

# %%
c.codes

# %%
c.categories

# %%
c = c.set_categories(['c1', 'c2', 'c3', 'c4', 'c5'])
c.categories

# %%
c.value_counts()

# %%
c[c.isin(['c1', 'c3'])]

# %%
c = c.remove_unused_categories()
c.categories

# %%
