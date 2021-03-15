# NumPy의 특징
# - Numerical Python의 약자
# - 고성능 과학 계산용 패키지로 강력한 N차원 배열 객체
# - 범용적 데이터 처리에 사용 가능한 다차원 컨데이터
# - 정교한 브로드캐스팅(broadcasting) 기능
# - 파이썬은 자료형 list와 비슷하지만, 더 빠르고 메모리를 효율적으로 관리
# - 데이터 과학 도구에 대한 생태계의 핵심을 이루고 있음
import numpy as np
np.__version__

a1 = np.array([1, 2, 3, 4, 5])
print(a1)
print(type(a1))
print(a1.shape)
print(a1[0], a1[1], a1[2], a1[3], a1[4])
a1[0] = 4
a1[1] = 5
a1[2] = 6
print(a1)

a2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a2)
print(a2.shape)
print(a2[1, 1], a2[2, 2], a2[0, 0])

a3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
               [[1, 2, 3], [2, 3, 4], [6, 7, 8]],
               [[2, 3, 4], [3, 4, 5], [4, 5, 6]],
               ])
print(a3)
print(a3.shape)

# 배열 생성 및 초기화
# - zeros() : 모든 요소를 0으로 초기화
np.zeros(10)

# - ones() : 모든 요소를 1로 초기화
np.ones(10)
np.ones((3, 3))

# full() : 모든 요소를 지정한 값으로 초기화
np.full((3, 3), 1.25)

# 단위행렬(identity matrix)생성
# - 주 대각선의 원소가 모두 1이고 나머지 원소는 모두 0인 정사각 행렬
np.eye(3)

# tri() : 삼각행렬 생성
np.tri(3)

# empty() : 초기화되지 않은 배열 생성
# - 초기화가 없어서 배열 생성비용이 저렴하고 생성속도가 빠름
# - 초기화가 되지 않아서 기존 메모리 위치에 존재하는 값이 있음(어떤값이 올 줄 모름)
np.empty(10)

# _like() : 지정된 배열과 shape가 같은 행렬 생성
# - np.zeros_like()
# - np.ones_like()
# - np.tri_like()
# - np.empty_like()
print(a1)
np.zeros_like(a1)
print(a2)
np.ones_like(a2)
print(a3)
np.full_like(a3, 10)

# 생성한 값으로 배열 생성
# arange() : 정수 범위로 배열 생성
np.arange(0, 30, 2)

# linspace() : 범위 내에서 균등 간격의 배열 생성
np.linspace(0, 1, 5)

# logspace() : 범위 내에서 균등간격으로 로그 스케일로 배열 생성
np.logspace(0.1, 1, 20)

# 랜덤 값으로 배열 생성
# random.random() : 랜덤한 수의 배열 생성
np.random.random((3, 3))

# random.randint() : 일정 구간의 랜덤 정수의 배열 생성
np.random.randint(0, 10, (3, 3))

# random.normal() : 정규분포(normal distribution)를 고려한 랜덤한 수의 배열 생성
# 평균 = 0, 표준편자 = 1, size = (n, m)
np.random.normal(0, 1, (3, 3))

# random.rand() : 균등분포(uniform distribution)를 고려한 랜덤한 수의 배열 생성
np.random.rand(3, 3)

# random.randn() : 표준 정규 분포(standard normal distribution)를 고려한 랜덤한 수의 배열 생성
np.random.randn(3, 3)

# 데이터 타입을 지정해서 생성 할 수 있다.
np.zeros(20, dtype=int)
np.ones((3, 3), dtype=bool)
np.full((3, 3), 1.0, dtype=float)

# 날짜 / 시간 배열 생성
# - 코드, 의미, 상대적 시간 범위, 절대적 시간 범위
date = np.array('2021-03-14', dtype=np.datetime64)
date
date + np.arange(12)
datetime = np.datetime64('2021-03-14 12:00:00')
datetime
datetime = np.datetime64('2021-03-14 13:00:00.15', 'ns')
datetime

# 26m5s
