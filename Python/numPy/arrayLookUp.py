# %%
from IPython import get_ipython
import numpy as np

# 배열 조회
# - 배열 속성 정보


# %%
def array_info(array):
    print("ndim: ", array.ndim)
    print("shape: ", array.shape)
    print("dtype: ", array.dtype)
    print("size: ", array.size)
    print("itemsize: ", array.itemsize)
    print("nbytes", array.nbytes)
    print("strides: ", array.strides)



# %%
a1 = np.array([1, 2, 3, 4, 5])
array_info(a1)


# %%
a2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array_info(a2)


# %%
a3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
               [[1, 2, 3], [2, 3, 4], [6, 7, 8]],
               [[2, 3, 4], [3, 4, 5], [4, 5, 6]],
               ])
array_info(a3)

# - 인덱싱(Indexing)


# %%
print(a1)
print(a1[0])
print(a1[2])
print(a1[-1])
print(a1[-2])


# %%
print(a2)

# %%
print(a2[0, 0])

# %%
print(a2[0, 2])

# %%
print(a2[1, 1])

# %%
print(a2[-2, -1])


# %%
print(a3)

# %%
print(a3[0, 0, 0])

# %%
print(a3[1, 1, 1])

# %%
print(a3[2, 2, 2])

# %%
print(a3[2, -1, -1])

# - 슬라이싱(Slicing))
#   - 슬라이싱 구문: a[start:stop:step]
#   - 기본값: start=0, stop=ndim, step=1


# %%
print(a1)
print(a1[0:2])
print(a1[0:])
print(a1[:1])
print(a1[::2])
print(a1[::-1])


# %%
print(a2)

# %%
print(a2[1])

# %%
print(a2[1, :])

# %%
print(a2[:2, :2])

# %%
print(a2[1:, ::-1])

# %%
print(a2[::-1, ::-1])

# 불리언 인덱싱(Boolean Indexing)
# - 배열 각 요소의 선택 여부를 불리언(boolean)으로 지정
# - True 값인 인덱스의 값만 조회


# %%
print(a1)
bi = [False, True, True, False, True]
print(a1[bi])


# %%
bi = [True, False, True, True, False]
print(a1[bi])


# %%
print(a2)
bi = np.random.randint(0, 2, (3, 3), dtype=bool)
print(bi)
print(a2[bi])

# 팬시 인덱싱(Fancy Indexing)


# %%
print(a1)
print([a1[0], a1[2]])

# %%
ind = [0, 2]
print(a1[ind])

# %%
ind = np.array([[0, 1],
                [2, 0]])
print(a1[ind])  # 1차원 array에 2차원 index를 주면 2차원으로 출력한다.


# %%
print(a2)
row = np.array([0, 2])
col = np.array([1, 2])
print(a2[row, col])

# %%
print(a2[row, :])

# %%
print(a2[:, col])

# %%
print(a2[row, 1])

# %%
print(a2[2, col])

# %%
print(a2[row, 1:])

# %%
print(a2[1:, col])
