# 데이터 결합

# Concat() / Append()

# %%
import numpy as np
import pandas as pd


# %%
s1 = pd.Series(['a', 'b'], index=[1, 2])
s2 = pd.Series(['c', 'd'], index=[3, 4])
pd.concat([s1, s2])


# %%
def create_df(cols, idx):
    data = {c: [str(c.lower())+ str(i) for i in idx] for c in cols}
    return pd.DataFrame(data, idx)


# %%
df1 = create_df('AB', [1, 2])
df1


# %%
df2 = create_df('AB', [3, 4])
df2


# %%
pd.concat([df1, df2])


# %%
df3 = create_df('AB', [0, 1])
df3


# %%
df4 = create_df('CD', [0, 1])
df4


# %%
pd.concat([df3, df4])


# %%
pd.concat([df3, df4], axis=1)


# %%
pd.concat([df1, df3])


# %%
# pd.concat([df1, df3], verify_integrity=True)


# %%
pd.concat([df1, df3], ignore_index=True)


# %%
pd.concat([df1, df3], keys=['X', 'Y'])


# %%
df5 = create_df('ABC', [1, 2])
df6 = create_df('BCD', [3, 4])
pd.concat([df5, df6])


# %%
pd.concat([df5, df6], join='inner')


# %%
df5.append(df6)

# %% [markdown]
# ### 병합과 조인

# %%
df1 = pd.DataFrame({'학생': ['홍길동', '이순신', '임꺽정', '김유신'],
                    '학과': ['경영학과', '교육학과', '컴퓨터학과', '통계학과']})
df1


# %%
df2 = pd.DataFrame({'학생': ['홍길동', '이순신', '임꺽정', '김유신'],
                    '입학년도': [2012, 2016, 2019, 2020]})
df2


# %%
df3 = pd.merge(df1, df2)
df3


# %%
df4 = pd.DataFrame({'학과': ['경영학과', '교육학과', '컴퓨터학과', '통계학과'],
                    '학과장': ['황희', '장영실', '안창호', '정약용']})
df4


# %%
pd.merge(df3, df4)


# %%
df5 = pd.DataFrame({'학과': ['경영학과', '교육학과', '교육학과', '컴퓨터학과', '컴퓨터학과', '통계학과'],
                    '과목' : ['경영개론', '기초수학', '물리학', '프로그래밍', '운영체제', '확률론']})
df5


# %%
pd.merge(df1, df5)


# %%
pd.merge(df1, df2, on='학생')


# %%
df6 = pd.DataFrame({'이름': ['홍길동', '이순신', '임꺽정', '김유신'],
                    '성적': ['A', 'A+', 'B', 'A+']})
df6


# %%
pd.merge(df1, df6, left_on='학생', right_on='이름')


# %%
pd.merge(df1, df6, left_on='학생', right_on='이름').drop('이름', axis=1)


# %%
mdf1 = df1.set_index('학생')
mdf2 = df2.set_index('학생')


# %%
mdf1


# %%
mdf2


# %%
pd.merge(mdf1, mdf2, left_index=True, right_index=True)


# %%
mdf1.join(mdf2)


# %%
pd.merge(mdf1, df6, left_index=True, right_on='이름')


# %%
df7 = pd.DataFrame({'이름': ['홍길동', '이순신', '임꺽정'],
                    '주문음식': ['햄버거', '피자', '짜장면']})
df7


# %%
df8 = pd.DataFrame({'이름': ['홍길동', '이순신', '김유신'],
                    '주문음료': ['콜라', '사이다', '커피']})
df8


# %%
pd.merge(df7, df8) # default 값은 inner


# %%
pd.merge(df7, df8, how='inner')


# %%
pd.merge(df7, df8, how='outer')


# %%
pd.merge(df7, df8, how='left')


# %%
pd.merge(df7, df8, how='right')


# %%
df9 = pd.DataFrame({'이름': ['홍길동', '이순신', '임꺽정', '김유신'],
                    '순위': [3, 2, 4, 1]})
df9


# %%
df10 = pd.DataFrame({'이름': ['홍길동', '이순신', '임꺽정', '김유신'],
                     '순위': [4, 1, 3 ,2]})
df10


# %%
pd.merge(df9, df10, on='이름')


# %%
pd.merge(df9, df10, on='이름', suffixes=['_인기', '_성적'])


# %%



