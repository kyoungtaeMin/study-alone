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

# 배열 값 삭제/복사

# 배열 값 삭제
# - delete(): 배열의 특정 위치에 값 삭제
# - axis를 지정하지 않으면 1차원 배열로 변환
# - 삭제할 방향을 asis로 지정
# - 원본 배열 변경없이 새로운 배열 반환


# %%
print(a1)


# %%
b1 = np.delete(a1, 1)
print(b1)


# %%
print(a2)


# %%
b2 = np.delete(a2, 1, axis=0)
print(b2)
c2 = np.delete(a2, 1, axis=1)
print(c2)


# 배열 복사
#   - 리스트 자료형과 달리 배열의 슬라이스는 복사본이 아님


# %%
print(a2)

# %%
print(a2[:2, :2])


# %%
a2_sub = a2[:2, :2]
print(a2_sub)

# %%
a2_sub[:, 1] = 0
print(a2_sub)

# %%
print(a2) # 원본 배열도 0의 값으로 바뀜 : 원본 배열에도 영향을 끼침

# - copy() : 배열이나 하위 배열 내의 값을 명시적으로 복사

# %%
print(a2)

# %%
a2_sub_copy = a2[:2, :2].copy()
print(a2_sub_copy)

# %%
a2_sub_copy[:, 1] = 1
print(a2_sub_copy)

# %%
print(a2) # 원본 배열의 값이 1로 변경되지 않음 : 영향 없음

