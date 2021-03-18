# %%
from IPython import get_ipython

# %% [markdown]
# ### 데이터 연산

# %%
import pandas as pd
import numpy as np


# %%
s = pd.Series(np.random.randint(1, 10, 5))
s


# %%
df = pd.DataFrame(np.random.randint(1, 10, (3, 3)),
                  columns=['A', 'B', 'C'])
df


# %%
np.exp(s)


# %%
np.cos((df* np.pi)/ 4)


# %%
s1 = pd.Series([1, 3, 5, 7, 9], index=[0, 1, 2, 3, 4])
s2 = pd.Series([2, 4, 6, 8, 10], index=[1, 2, 3, 4, 5])
s1+ s2 # index기준으로 연산


# %%
s1.add(s2, fill_value=0) # 없는 값은 0으로 대체


# %%
df1 = pd.DataFrame(np.random.randint(0, 20, (3, 3)),
                   columns=list('ACD'))
df1


# %%
df2 = pd.DataFrame(np.random.randint(0, 20, (5, 5)),
                   columns=list('BAECD'))
df2


# %%
df1+ df2


# %%
fvalue = df1.stack().mean()
df1.add(df2, fill_value=fvalue)

# %% [markdown]
# ### 연산자 범용 함수

# %%
a = np.random.randint(1, 10, size=(3, 3))
a


# %%
a+ a[0]


# %%
df = pd.DataFrame(a, columns=list('ABC'))
df


# %%
df+ df.iloc[0]


# %%
df.add(df.iloc[0])


# %%
a


# %%
a- a[0]


# %%
df


# %%
df- df.iloc[0]


# %%
df.sub(df.iloc[0])


# %%
df.subtract(df['B'], axis=0)


# %%
a


# %%
a* a[1]


# %%
df


# %%
df* df.iloc[1]


# %%
df.mul(df.iloc[1])


# %%
df.multiply(df.iloc[1])

# %% [markdown]
# ### truediv() / div() / divide() / floordiv()

# %%
a


# %%
a/ a[0]


# %%
df


# %%
df/ df.iloc[0]


# %%
df.truediv(df.iloc[0])


# %%
df.div(df.iloc[1])


# %%
df.divide(df.iloc[2])


# %%
a// a[0]


# %%
df.floordiv(df.iloc[0])

# %% [markdown]
# ### mod()

# %%
a


# %%
a% a[0]


# %%
df.mod(df.iloc[0])

# %% [markdown]
# ### pow()]

# %%
a


# %%
a** a[0]


# %%
df


# %%
df.pow(df.iloc[0])


# %%
row = df.iloc[0, ::2]
row


# %%
df- row

# %% [markdown]
# ### 정렬 (Sort)

# %%
s = pd.Series(range(5), index=['A', 'D', 'B', 'C', 'E'])
s


# %%
s.sort_index()


# %%
s.sort_values()


# %%
df = pd.DataFrame(np.random.randint(0, 10, size=(4, 4)),
                  index=[2, 4, 1, 3],
                  columns=list('BDAC'))
df


# %%
df.sort_index()


# %%
df.sort_index(axis=1)


# %%
df.sort_values(by='A')


# %%
df.sort_values(by=['A', 'C'])

# %% [markdown]
# ### 순위 (Rnaking)

# %%
s = pd.Series([-3, 7, -6, 3, 5, 6, 7, 9, 4])
s


# %%
s.rank() # 작은 순서부터 1위로 순위를 매김, 같은 값은 .5로 표현


# %%
s.rank(method='first') # 같은 값이 있으면 index순으로 순위를 매김


# %%
s.rank(method='max') # 같은 값이 있으면 높은 순위로 매김

# %% [markdown]
# ### 고성능 연산

# %%
nrows, ncols = 100000, 100
df1, df2, df3, df4 = (pd.DataFrame(np.random.rand(nrows, ncols)) for i in range(4))


# %%
get_ipython().run_line_magic('timeit', '(df1+ df2+ df3+ df4)')


# %%
get_ipython().run_line_magic('timeit', "pd.eval('df1+ df2+ df3+ df4')")


# %%
get_ipython().run_line_magic('timeit', 'df1* df2/ (-df3* df4)')


# %%
get_ipython().run_line_magic('timeit', 'pd.eval(df1* df2/ (-df3* df4))')


# %%
get_ipython().run_line_magic('timeit', '(df1 < df2) & (df2 <= df3) & (df3 != df4)')


# %%
get_ipython().run_line_magic('timeit', 'pd.eval((df1 < df2) & (df2 <= df3) & (df3 != df4))')


# %%
df = pd.DataFrame(np.random.rand(1000000, 5), columns=['A', 'B', 'C', 'D', 'E'])
df.head()


# %%
get_ipython().run_line_magic('timeit', "(df['A']+ df['B']/ df['C']- df['D']* df['E'])")


# %%
get_ipython().run_line_magic('timeit', "pd.eval('df.A+ df.B/ df.C- df.D* df.E')")


# %%
get_ipython().run_line_magic('timeit', "df.eval('A+ B/ C- D* E')")


# %%
df.eval('R = A+ B/ C- D* E', inplace=True)
df.head()


# %%
col_mean = df.mean(1)


# %%
df['A']+ col_mean


# %%
df.eval('A+ @col_mean') # 외부에 있는 변수를 @로 불러올 수 있다.


# %%
df[(df.A< 0.5)& (df.B<0.5)& (df.C> 0.5)]


# %%
pd.eval('df[(df.A< 0.5)& (df.B<0.5)& (df.C> 0.5)]')


# %%
df.query('(A< 0.5)and (B< 0.5)and (C> 0.5)')


# %%
col_mean = df['D'].mean()


# %%
df[(df.A< col_mean)& (df.B< col_mean)]


# %%
df.query('A< @col_mean and B< @col_mean')


# %%



