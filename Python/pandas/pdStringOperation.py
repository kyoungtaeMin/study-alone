# %%
import numpy as np
import pandas as pd

# %%
# 문자열 연산
# - 파이썬의 문자열 연산자를 거의 모두 반영

# %%
name_tuple = ['Suan Lee', 'Stevan Jobs', 'Larry Page', 'Elon Musk',
              None, 'Bill Gates', 'Mark Zuckerberg', 'Jeff Bezos']
names = pd.Series(name_tuple)
names

# %%
names.str.lower()

# %%
names.str.len()

# %%
names.str.split()

# %%
# 기타 연산자

# %%
names.str[0:4]

# %%
names.str.split().str.get(-1)

# %%
names.str.repeat(2)

# %%
names.str.join('*')

# %%
# 정규표현식

# %%
names.str.match('([A-Za-z]+)')

# %%
names.str.findall('([A-Za-z]+)')

