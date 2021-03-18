# 배열 연산
# - NumPy의 배열 연산은 백터화(vectorized) 연산을 사용
# - 일반적으로 NumPy의 범용 함수(universla function)를 통해 구현
# - 배열 요소에 대한 반복적인 계산을 효율적으로 수행

# 브로드캐스팅(Broadcasting)

# [1, 2, 3] + [5] = [6, 7, 8]

# [1, 2, 3] + [[1, 2, 3], = [[2, 4, 6],
#              [4, 5, 6],    [5, 7, 9],
#              [7, 8, 9]]    [8, 10, 12]]

# [1, 2, 3] + [1, = [[2, 3, 4],
#              2,    [3, 4, 5],
#              3]    [4, 5, 6]]


# %%
from IPython import get_ipython
import numpy as np


# %%
a1 = np.array([1, 2, 3])
print(a1)
print(a1+ 5)


# %%
a2 = np.arange(1, 10).reshape(3, 3)
print(a2)
print(a1+ a2)


# %%
b2 = np.array([1, 2, 3]).reshape(3, 1)
print(b2)
print(a1+ b2)


# %%
# 산술 연산 (Arithmetic Operators)
a1 = np.arange(1, 10)
print(a1)


# %%
print(a1+ 1)
print(np.add(a1, 10)) # 더하기


# %%
print(a1- 2)
print(np.subtract(a1, 10)) # 빼기


# %%
print(-a1)
print(np.negative(a1)) # 음수로 변환


# %%
print(a1* 2)
print(np.multiply(a1, 2)) # 곱하기


# %%
print(a1/ 2)
print(np.divide(a1, 2)) # 나누기


# %%
print(a1// 2)
print(np.floor_divide(a1, 2)) # 몫


# %%
print(a1** 2)
print(np.power(a1, 2)) # 제곱


# %%
print(a1% 2)
print(np.mod(a1, 2)) # 나머지


# %%
a1 = np.arange(1, 10)
print(a1)
b1 = np.random.randint(1, 10, size=9)
print(b1)


# %%
print(a1+ b1)
print(a1- b1)
print(a1* b1)
print(a1/ b1)
print(a1** b1)
print(a1// b1)
print(a1% b1)


# %%
a2 = np.arange(1, 10).reshape(3, 3)
print(a2)
b2 = np.random.randint(1, 10, size=(3, 3))
print(b2)


# %%
print(a2+ b2)
print(a2- b2)
print(a2* b2)
print(a2/ b2)
print(a2** b2)
print(a2// b2)
print(a2% b2)


# %%
# 절대값 함수 (Absolute Function)
#   - absolute(), abs() : 내장된 절대값 함수
a1 = np.random.randint(-10, 10, size=5)
print(a1)
print(np.absolute(a1))
print(abs(a1))


# %%
# 제곱 / 제곱근 함수
#   - square(), sqrt() : 제곱, 제곱근 함수
print(a1)
print(np.square(a1))
print(np.sqrt(a1))


# %%
# 지수와 로그 함수 (Exponantial and Log Function)
a1 = np.random.randint(1, 10, size=5)
print(a1)
print(np.exp(a1))
print(np.exp2(a1))
print(np.power(a1, 2))


# %%
print(a1)
print(np.log(a1))
print(np.log2(a1))
print(np.log10(a1))


# %%
# 삼각 함수 (Trigonometrical Function)
t = np.linspace(0, np.pi, 3)
print(t)
print(np.sin(t))
print(np.cos(t))
print(np.tan(t))


# %%
x = [-1, 0, 1]
print(x)
print(np.arcsin(x))
print(np.arccos(x))
print(np.arctan(x))


# %%
# 집계 함수 (Aggregate Function)
#   - sum() : 합 계산
a2 = np.random.randint(1, 10, size=(3, 3))
print(a2)
print(a2.sum(), np.sum(a2))
print(a2.sum(axis=0), np.sum(a2, axis=0))
print(a2.sum(axis=1), np.sum(a2, axis=1))


# %%
print(a2)
print(a2.cumsum(), np.cumsum(a2))
print(a2.cumsum(axis=0), np.cumsum(a2, axis=0))
print(a2.cumsum(axis=1), np.cumsum(a2, axis=1))


# %%
# diff() : 차분 계산
print(a2)
print(np.diff(a2)) # default = 1
print(np.diff(a2, axis=0))
print(np.diff(a2, axis=1))


# %%
# prod() : 곱 계산
print(a2)
print(np.prod(a2))
print(np.prod(a2, axis=0))
print(np.prod(a2, axis=1))


# %%
# cumprod() : 누적 곱 계산
print(a2)
print(np.cumprod(a2))
print(np.cumprod(a2, axis=0))
print(np.cumprod(a2, axis=1))


# %%
# dot() / matmul() : 점곱 / 행렬곱 계산
print(a2)
b2 = np.ones_like(a2)
print(b2)
print(np.dot(a2, b2))
print(np.matmul(a2, b2))


# %%
# tensordot() : 텐서곱 계산
print(a2)
print(b2)
print(np.tensordot(a2, b2))
print(np.tensordot(a2, b2, axes=0))
print(np.tensordot(a2, b2, axes=1))


# %%
# corss() : 벡터곱 계산
x = [1, 2, 3]
y = [4, 5, 6]
print(np.cross(x, y))


# %%
# inner()/outer() : 내적/외적
print(a2)
print(b2)
print(np.inner(a2, b2))
print(np.outer(a2, b2))


# %%
# mean() : 평균 계산
print(a2)
print(np.mean(a2))
print(np.mean(a2, axis=0))
print(np.mean(a2, axis=1))


# %%
# std() : 표준편차 계산
print(a2)
print(np.std(a2))
print(np.std(a2, axis=0))
print(np.std(a2, axis=1))


# %%
# var() : 분산 계산
print(a2)
print(np.var(a2))
print(np.var(a2, axis=0))
print(np.var(a2, axis=1))


# %%
# min() : 최소값
print(a2)
print(np.min(a2))
print(np.min(a2, axis=0))
print(np.min(a2, axis=1))


# %%
# max() : 최대값
print(a2)
print(np.max(a2))
print(np.max(a2, axis=0))
print(np.max(a2, axis=1))


# %%
# argmin() : 최소값 인덱스 (최소값의 위치를 나타냄)
print(a2)
print(np.argmin(a2))
print(np.argmin(a2, axis=0))
print(np.argmin(a2, axis=1))


# %%
# argmax() : 최대값 인덱스 (최대값의 위치를 나타냄)
print(a2)
print(np.argmax(a2))
print(np.argmax(a2, axis=0))
print(np.argmax(a2, axis=1))


# %%
# median() : 중앙값
print(a2)
print(np.median(a2))
print(np.median(a2, axis=0))
print(np.median(a2, axis=1))


# %%
# percentile() : 백분위 수
a1 = np.array([0, 1, 2, 3])
print(a1)
print(np.percentile(a1, [0, 20, 40, 60, 80, 100], interpolation='linear'))
print(np.percentile(a1, [0, 20, 40, 60, 80, 100], interpolation='higher'))
print(np.percentile(a1, [0, 20, 40, 60, 80, 100], interpolation='lower'))
print(np.percentile(a1, [0, 20, 40, 60, 80, 100], interpolation='nearest'))
print(np.percentile(a1, [0, 20, 40, 60, 80, 100], interpolation='midpoint'))


# %%
# any()
a2 = np.array([[False, False, False],
               [False, True, True],
               [False, True, True]])
print(a2)
print(np.any(a2))
print(np.any(a2, axis=0))
print(np.any(a2, axis=1))


# %%
# all()
a2 = np.array([[False, False, True],
               [True, True, True],
               [False, True, True]])
print(a2)
print(np.all(a2))
print(np.all(a2, axis=0))
print(np.all(a2, axis=1))


# %%
# 비교 연산 (Comparison Operators)
a1 = np.arange(1, 10)
print(a1)


# %%
print(a1== 5)
print(a1!= 5)
print(a1< 5)
print(a1<= 5)
print(a1> 5)
print(a1>= 5)


# %%
a2 = np.arange(1, 10).reshape(3, 3)
print(a2)
print(np.sum(a2))
print(np.count_nonzero(a2> 5))
print(np.sum(a2> 5))
print(np.sum(a2> 5, axis=0))
print(np.sum(a2> 5, axis=1)) # ※ 갯수를 알려준다


# %%
print(np.any(a2> 5))
print(np.any(a2> 5, axis=0))
print(np.any(a2> 5, axis=1)) # ※ bool형태 1개라도 있으면 True


# %%
print(np.all(a2> 5))
print(np.all(a2> 5, axis=0))
print(np.all(a2> 5, axis=1)) # ※ bool형태 전체가 모두 True이어야 True


# %%
# 비교 범용 함수
a1 = np.array([1, 2, 3, 4, 5])
print(a1)
b1 = np.array([1, 2, 3, 3, 4])
print(b1)
print(np.isclose(a1, b1)) # 두 array를 비교해서 같은 위치의 값이 같으면 True, 다르면 False


# %%
a1 = np.array([np.nan, 2, np.inf, 4, np.NINF])
print(a1)
print(np.isnan(a1))
print(np.isinf(a1))
print(np.isfinite(a1))


# %%
# 불리언 연산자 (Boolean Operators)
a2 = np.arange(1, 10).reshape(3, 3)
print(a2)


# %%
print((a2> 5)& (a2< 8))
print(a2[(a2> 5)& (a2< 8)]) # a2의 조건으로 넣어서 실제 값을 출력할 수 있다


# %%
print((a2> 5)| (a2< 8))
print(a2[(a2> 5)| (a2< 8)])


# %%
print((a2> 5)^ (a2< 8))
print(a2[(a2> 5)^ (a2< 8)]) # 배타적 OR 연산


# %%
print(~(a2> 5))
print(a2[~(a2> 5)]) # not