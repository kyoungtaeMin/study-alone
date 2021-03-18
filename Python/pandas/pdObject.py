# Pandas 특징
# - 관계 또는 레이블링 데이터로 쉽고 직관적으로 작업할 수 있도록 고안된 빠르고 유연하며 표현력이 뛰어난 데이터 구조를 제공하는 Python 패키지
# - 부동 소수점이 아닌 데이터 뿐만 아니라 부동 소수점 데이터에서도 결측 데이터(NaN으로 표시됨)를 쉽게 처리
# - 크기 변이성(Size mutability) : DataFrame 및 고차원 객체에서 열음 삽입 및 삭제 가능
# - 자동 및 명시적(explicit) 데이터 정렬 : 객체를 라벨 집합에 명시적으로 정렬하거나, 사용자가 라벨을 무시하고 Series, DataFrame 등의 계산에서 자동으로 데이터 조정 가능
# - 데이터 세트에서 집계 및 변환을 위한 분할(split), 적용(apply), 결합(combine) 작업을 수행할 수 있는 강력하고 유연한 group-by 함수 제공
# - 누락된 데이터 또는 다른 Python 및 NumPy 데이터 구조에서 서로 다른 인뎅싱 데이터를 DateFrame 개체로 쉽게 변환
# - 대용량 데이터 세트의 지능형 라벨 기반 슬라이싱, 고급 인뎅싱 및 부분 집합 구하기 가능
# - 축의 계층적 라벨링(눈금당 여러 개의 라벨을 가질 수 있음)
# - 플랫 파일(CSV 및 구분), Excel 파일, 데이터베이스 로딩 및 초고속 HDF5 형식의 데이터 저장/로드에 사용되는 강령한 IO도구
# - 시계열 특정 기능 : 날짜 범위 생성 및 주파수 변환, 무빙 윈도우(moving window) 통계, 날짜 이동 및 지연
# - NumPy를 기반으로 만들어짐

# %%
from IPython import get_ipython
import numpy as np
import pandas as pd

# Pandas Objects

#  Series Object

# %%
s = pd.Series([0, 0.25, 0.5, 0.75, 1.0])
s

# %%
s.values

# %%
s.index

# %%
s[1]

# %%
s[1:3]

# %%
s = pd.Series([0, 0.25, 0.5, 0.75, 1.0],
              index=['a', 'b', 'c', 'd', 'e'])
s

# %%
s['c']

# %%
s[['c', 'd', 'e']]

# %%
'b' in s

# %%
s = pd.Series([0, 0.25, 0.5, 0.75, 1.0],
              index=[2, 5, 6, 7, 9])
s

# %%
s[7]

# %%
s[2:]

# %%
s.unique()

# %%
s.value_counts()

# %%
s.isin([0.25, 0.75, 0.7])

# %%
pop_tuple = {'서울특별시': 9720846,
             '부산광역시': 3404423,
             '인천광역시': 2947217,
             '대구광역시': 2427954,
             '대전광역시': 1471040,
             '광주광역시': 1455048}
population = pd.Series(pop_tuple)
population

# %%
population['대전광역시']

# %%
population['대구광역시': '광주광역시']

# DataFrame Object

# %%
pd.DataFrame([{'A': 2, 'B': 4, 'D': 6},
              {'A': 3, 'B': 6, 'C': 9}])

# %%
pd.DataFrame(np.random.rand(5, 5),
             columns=['a', 'b', 'c', 'd', 'e'],
             index=[1, 2, 3, 4, 5])

# %%
male_tuple = {'서울특별시': 4732275,
              '부산광역시': 1668618,
              '인천광역시': 1476813,
              '대구광역시': 1198815,
              '대전광역시': 734441,
              '광주광역시': 720060}
male = pd.Series(male_tuple)
male

# %%
female_tuple = {'서울특별시': 4988571,
                '부산광역시': 1735805,
                '인천광역시': 1470404,
                '대구광역시': 1229139,
                '대전광역시': 736599,
                '광주광역시': 734988}
female = pd.Series(female_tuple)
female

# %%
korea_df = pd.DataFrame({'총인구수': population,
                         '남자인구수': male,
                         '여자인구수': female})
korea_df

# %%
korea_df.index

# %%
korea_df.columns

# %%
korea_df['여자인구수']

# %%
korea_df['서울특별시': '대전광역시']

# Index Object

# %%
idx = pd.Index([2, 4, 6, 8, 10])
idx

# %%
idx[1]

# %%
idx[0:4:2]

# %%
idx[-1::]

# %%
idx[::2]

# %%
print(idx)
print(idx.size)
print(idx.shape)
print(idx.ndim)
print(idx.dtype)
