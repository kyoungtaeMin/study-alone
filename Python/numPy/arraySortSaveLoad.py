# %%
from IPython import get_ipython
import numpy as np

# 배열 정렬


# %%
a1 = np.random.randint(1, 10, size=10)
print(a1)

# %%
print(np.sort(a1)) # 정렬된 결과를 보여줌 ※ 정렬된 결과가 a1에 저장이 되지 않음

# %%
print(np.argsort(a1)) # 정렬된 자리에 와야할 값의 위치를 보여줌


# %%
print(a1.sort()) # 정렬된 결과가 저장됨

# %%
print(a1)


# %%
a2 = np.random.randint(1, 10, size=(3, 3))
print(a2)

# %%
print(np.sort(a2, axis=0))

# %%
print(np.sort(a2, axis=1))

# 부분 정렬
#   - partition() : 배열에서 k개의 작은 값을 반환

# %%
a1 = np.random.randint(1, 10, size=10)
print(a1)

# %%
print(np.partition(a1, 3))


# %%
a2 = np.random.randint(1, 10, size=(5, 5))
print(a2)

# %%
print(np.partition(a2, 3))

# %%
print(np.partition(a2, 3, axis=0))

# %%
print(np.partition(a2, 3, axis=1))

# 배열 입출력

# %%
a2 = np.random.randint(1, 10, size=(5, 5))
print(a2)

# %%
np.save('a', a2)

# %%
b2 = np.random.randint(1, 10, size=(5, 5))
print(b2)
np.savez('ab', a2, b2)


# %%
npy = np.load('a.npy')
print(npy)


# %%
npz = np.load('ab.npz')
print(npz.files)

# %%
print(npz['arr_0'])
print(npz['arr_1'])


# %%
print(a2)

# %%
np.savetxt('a.csv', a2, delimiter=',')

# %%
csv = np.loadtxt('a.csv', delimiter=',')
print(csv)


# %%
print(b2)

# %%
np.savetxt('b.csv', b2, delimiter=',', fmt='%.2e', header='c1, c2, c3, c4, c5')


# %%
csv = np.loadtxt('b.csv', delimiter=',')
print(csv)

# www.numpy.org