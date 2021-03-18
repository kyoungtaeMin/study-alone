# %%
from IPython import get_ipython
import numpy as np


# %%
a1 = np.array([1, 2, 3, 4, 5])
a2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
               [[1, 2, 3], [2, 3, 4], [6, 7, 8]],
               [[2, 3, 4], [3, 4, 5], [4, 5, 6]],
               ])


# 배열 값 삽입

# - insert(): 배열의 특정 위치에 값 삽입
# - axis를 지정하지 않으면 1차원 배열로 변환
# - 추가할 방향을 axis로 지정
# - 원본 배열 변경없이 새로운 배열 반환

# %%
print(a1)

# %%
b1 = np.insert(a1, 0, 10) # a1에 0번째에 값은 10 삽입
print(b1)

# %%
c1 = np.insert(a1, 2, 10)
print(c1)


# %%
print(a2)

# %%
b2 = np.insert(a2, 1, 10, axis=0)
print(b2)

# %%
c2 = np.insert(a2, 1, 10, axis=1)
print(c2)

# 배열 값 수정
# - 배열의 인덱싱으로 접근하여 값 수정

# %%
print(a1)

# %%
a1[0] = 7
a1[1] = 6
a1[2] = 5
a1[3] = 4
a1[4] = 3
print(a1)


# %%
a1[:1] = 9
print(a1)


# %%
i = np.array([1, 3, 4])
a1[i] = 0
print(a1)


# %%
a1[i] += 4
print(a1)


# %%
print(a2)

# %%
a2[0, 0] = 1
a2[1, 1] = 2
a2[2, 2] = 3
a2[0] = 4 # 2차원 배열에서 하나의 인덱스만 입력하면 행 전체가 모두 바뀐다.
print(a2)


# %%
a2[1:, 2] = 9
print(a2)


# %%
row = np.array([0, 1])
col = np.array([1, 2])
a2[row, col] = 0
print(a2)
