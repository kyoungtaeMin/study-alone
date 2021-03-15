import math
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

# 신경망 기초 수학

# 일차함수
# y = ax + b
# - a : 기울기, b : y절편
# 그래프 상에서 직선인 그래프(linear)


def linear_function(x):
    a = 0.5
    b = 2
    return a*x + b


print(linear_function(5))
x = np.arange(-5, 5, 0.1)
y = linear_function(x)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Function')
plt.show()


# 이차함수
# - y = a(x**2) + bx + c
# - 일반적으로 두 개의 실근을 가짐
def quadratic_function(x):
    a = 1
    b = -1
    c = -2
    return a*(x**2) + (b*x) + c


print(quadratic_function(2))
x = np.arange(-5, 5, 0.1)
y = quadratic_function(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic Function')
plt.show()


# 삼차함수(다항함수)
# - y = a(x**3) + b(x**2) + cx + d
def cubic_function(x):
    a = 4
    b = 0
    c = -1
    d = -8
    return a*(x**3) + b*(x**2) + (c*x) + d


print(cubic_function(3))
x = np.arange(-5, 5, 0.1)
y = cubic_function(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Cubic Function')
plt.show()


# 함수의 최소값/최대값
def func(x):
    a = 1
    b = -3
    c = 10
    return a*(x**2) + (b*x) + c

x = np.arange(-10, 10, 0.1)
y = func(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(1.5, func(1.5))
plt.text(1.5-1.5, func(1.5)+10,
         'min value of f(x)\n({}, {})'.format(1.5, func(1.5)), fontsize=10)
plt.title('func')
plt.show()
min_val = min(y)
print(min_val)

# 14m 49s