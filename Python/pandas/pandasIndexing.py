import numpy as np
import pandas as pd

# 인덱싱 (Indexing)

idx1 = pd.Index([1, 2, 4, 6, 8])
idx2 = pd.Index([2, 4, 5, 6, 7])
print(idx1.append(idx2))
print(idx1.difference(idx2))
print(idx1.intersection(idx2)) # 공통되는 부분을 출력
print(idx1 & idx2)
print(idx1.union(idx2)) # 중복된 값은 빼고 합집합
print(idx1 | idx2)
print(idx1.delete(0))
print(idx1.drop(1))
print(idx1 ^ idx2) # 공통되는 부분은 빼고 나머지를 합친다

# - Series

s = pd.Series([1, 2, 3, 4, 5],
              index = ['a', 'b', 'c', 'd', 'e'])
s
s['b']
'b' in s
s.keys() # 인덱스 값 출력
s.items() # zip으로 압축되어 옴
list(s.items()) # 그래서 list를 사용해서 풀어서 출력
s['f'] = 6
s
s['a': 'd'] # 인덱스로 슬라이싱 가능
s[0: 4] # 순번으로 슬라이싱 가능
s[(s > 1) & (s < 6)] # 슬라이싱 할 때, 필터링 가능
s[[1, 4, 5]]
s[['b', 'e', 'f']] # 원하는 부분만 뽑기 가능 (대괄호 주의)

s = pd.Series(['a', 'b', 'c', 'd', 'e'],
              index=[1, 3, 5, 7, 9])
s
s.iloc[1] # iloc는 정수값으로 계산하기 때문에 1이면 두번째 값 출력
s.iloc[2: 4]
s.reindex(range(10)) # index 다시 함. 비어있는 칸은 NaN로 채워짐
s.reindex(range(10), method='bfill') # 비어있는 칸을 뒤에 위치한 값들로 채움

#  - DataFrame

korea_df
korea_df['남자인구수']
korea_df.남자인구수
korea_df.여자인구수
korea_df['남여비율'] = (korea_df['남자인구수']* 100/ korea_df['여자인구수'])
korea_df.남여비율
korea_df.values
korea_df.T
korea_df.values[0]

korea_df.loc[:'부산광역시', :'남자인구수']

korea_df.loc[korea_df.여자인구수 > 1000000]
korea_df.loc[korea_df.총인구수 < 2000000]
korea_df.loc[korea_df.총인구수 > 2500000]
korea_df.loc[korea_df.남여비율 > 100]

korea_df.loc[(korea_df.총인구수 > 2500000)& (korea_df.남여비율 > 100)]

korea_df.iloc[:3, :2]

# 다중 인덱싱(Multi Indexing)
# - 1차원의 Series와 2차원의 DataFrame 객체를 넘어 3차원, 4차원 이상의 고차원 데이터 처리
# - 단일 인덱스 내에 여러 인덱스를 포함하는 다중 인덱싱

#   - 다중 인덱스 Series
korea_df
idx_tuples = [('서울특별시', 2010), ('서울특별시', 2020),
              ('부산광역시', 2010), ('부산광역시', 2020),
              ('인천광역시', 2010), ('인천광역시', 2020),
              ('대구광역시', 2010), ('대구광역시', 2020),
              ('대전광역시', 2010), ('대전광역시', 2020),
              ('광주광역시', 2010), ('광주광역시', 2020)]
pop_tuples = [10312545, 9720846,
              2567910, 3404423,
              2758296, 2947217,
              2511676, 2427954,
              1503664, 1471040,
              1454636, 1455048]
population = pd.Series(pop_tuples, index=idx_tuples)
population
midx = pd.MultiIndex.from_tuples(idx_tuples)
midx
population = population.reindex(midx)
population
population[:, 2010]
population['대전광역시', :]

korea_mdf = population.unstack()
korea_mdf
korea_mdf.stack()

male_tuples = [5111259, 4732275,
              1773170, 1668618,
              1390356, 1476813,
              1255245, 1198815,
              753648, 734441,
              721780, 720060]
male_tuples
korea_mdf = pd.DataFrame({'총인구수': population,
                         '남자인구수': male_tuple})
korea_mdf

female_tuples = [5201286, 4988571,
                 1794740, 1735805,
                 1367940, 1470404,
                 1256431, 1229139,
                 750016, 736599,
                 732856, 734988]
female_tuples
korea_mdf = pd.DataFrame({'총인구수': population,
                          '남자인구수': male_tuples,
                          '여자인구수': female_tuples})
korea_mdf

ratio = korea_mdf['남자인구수']* 100/ korea_mdf['여자인구수']
ratio
ratio.unstack()
korea_mdf = pd.DataFrame({'총인구수': population,
                          '남자인구수': male_tuples,
                          '여자인구수': female_tuples,
                          '남여비율': ratio})
korea_mdf

# 56m 18s