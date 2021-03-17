import numpy as np

a1 = np.array([1, 2, 3, 4, 5])
a2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
               [[1, 2, 3], [2, 3, 4], [6, 7, 8]],
               [[2, 3, 4], [3, 4, 5], [4, 5, 6]],
               ])

# 배열 변환
# - 배열 전치 및 축 변경
print(a2)
print(a2.T)

print(a3)
print(a3.T)

print(a2)
print(a2.swapaxes(1, 0))

print(a3)
print(a3.swapaxes(0, 1))
print(a3.swapaxes(1, 2))

# 배열 재구조화
#   - reshape() : 배열의 형상을 변경
n1 = np.arange(1, 10)
print(n1)
print(n1.reshape(3,3))

# newaxis() = 새로운 축 추가
print(n1)
print(n1[np.newaxis, : 5])
print(n1[: 5, np.newaxis])

# 배열 크기 변경
#   - 배열 모양만 변경
n2 = np.random.randint(0, 10, (2, 5))
print(n2)
n2.resize((5, 2))
print(n2)

# 배열 크기 증가
# - 남은 공간은 0으로 채워짐
n2.resize((5, 5), refcheck=False)
print(n2)

# 배열 크기 감소
# - 포함되지 않은 값은 삭제됨
n2.resize((3, 3), refcheck=False)
print(n2)

# 배열 추가
#   - append() : 배열의 끝에 값 추가
a2 = np.arange(1, 10).reshape(3, 3)
print(a2)
b2 = np.arange(10, 19).reshape(3, 3)
print(b2)

# axis 지정이 없으면 1차원 배열 형태로 변형되어 결합
c2 = np.append(a2, b2)
print(c2)

# axis를 0으로지정
#   - shape[0]을 제외한 나머지 shape은 같아야 함
c2 = np.append(a2, b2, axis=0)
print(c2)

# axis를 1으로지정
#   - shape[1]을 제외한 나머지 shape은 같아야 함
c2 = np.append(a2, b2, axis=1)
print(c2)

# 배열 연결
#   - concatenate() : 튜플이나 배열의 리스트를 인수로 사용해 배열 연결
a1 = np.array([1, 3, 5])
b1 = np.array([2, 4, 6])
np.concatenate([a1, b1])
c1 = np.array([7, 8, 9])
np.concatenate([a1, b1, c1])

a2 = np.array([[1, 2, 3],
               [4, 5, 6]])
np.concatenate([a2, a2]) # default의 axis = 0

a2 = np.array([[1, 2, 3],
               [4, 5, 6]])
np.concatenate([a2, a2], axis=1)

#   - vstack() : 수직 스택(vertical stack), 1차원으로 연결
np.vstack([a2, a2])

#   - hstack() : 수평 스택(horizontal stack), 2차원으로 연결
np.hstack([a2, a2])

# stack() : 새로운 차원으로 연결
np.stack([a2, a2])

# 배열 분할
#   - split() : 배열 분할
a1 = np.arange(0, 10)
print(a1)
b1, c1 = np.split(a1, [5])
print(b1, c1)
b1, c1, d1, e1, f1 = np.split(a1, [2, 4, 6, 8])
print(b1, c1, d1, e1, f1)

# vsplit() : 수직분할, 1차원으로 분할
a2 = np.arange(1, 10).reshape(3, 3)
print(a2)
b2, c2 = np.vsplit(a2, [2])
print(b2)
print(c2)

# hsplit() : 수평분할, 2차원으로 분할
a2 = np.arange(1, 10).reshape(3, 3)
print(a2)
b2, c2 = np.hsplit(a2, [2])
print(b2)
print(c2)

# dsplit() : 깊이 분할, 3차원으로 분할
a3 = np.arange(1, 28).reshape(3, 3, 3)
print(a3)
b3, c3 = np.dsplit(a3, [2])
print(b3)
print(c3)
