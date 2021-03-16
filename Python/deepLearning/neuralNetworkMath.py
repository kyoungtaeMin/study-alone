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

# 특정 구간 내에서 최소값 구하기

def get_minimum(x1, x2, f):
    x = np.arange(x1, x2, 0.01)
    y = f(x)

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('get_minimum')
    plt.show()

    return min(y)
print(get_minimum(1, 4, func))

# 지수함수 / 로그함수
# - 지수함수, 로그함수는 역함수 관계(y = x직선 대칭  단, 밑이 같을 때)
# - 파이썬으로 직접 구현 가능

# 지수함수
#   y = a**x (a!= 0)(기본형)
#   y = e**x (e = 2.71828...)
def exponential_function(x):
    a = 4
    return a**x

print(exponential_function(4))
print(exponential_function(0))

x = np.arange(-3, 2, 0.1)
y = exponential_function(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-1, 15) # lim은 limit를 뜻함
plt.xlim(-4, 3)
plt.title("exponential_function")
plt.show()

def exponential_function2(x):
    a = 4
    return math.pow(a, x)

print(exponential_function2(4))
print(exponential_function2(0))

# 밑이 e인 지수함수 표현
print(math.exp(4))
print(np.exp(4))

# 로그함수
#   y = loga(x) (a!= 1)(기본형)
#   y = log10(x)(상용로그)
#   y = ln(x)(밑이 e인 자연로그)
print(math.log(2, 3))
print(np.log2(4))
print(np.log(4))

# 역함수 관계
#   y = x 대칭
x = np.arange(-1, 5, 0.01)
y1 = np.exp(x)

x2 = np.arange(0.000001, 5, 0.01)
y2 = np.log(x2)

y3 = x

plt.plot(x, y1, 'r-', x2, y2, 'b-', x, y3, 'k--')
plt.ylim(-2, 6)
plt.axvline(x=0, color='k')
plt.axhline(y=0, color='k')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# 역함수 관계
#   y = -loga(x)와 y = -loga(1-x)
#   x = 0.5 대칭
#   Logistic Regression을 위한 함수
x = np.arange(-10, 10, 0.01)
y1 = -np.log(x)
y2 = -np.log(1-x)

plt.axvline(x=0, color='k')
plt.axhline(y=0, color='k')

plt.grid()
plt.plot(x, y1, 'b-', x, y2, '-r')
plt.text(0.9, 2.0, 'y = -log(1-x)', fontsize=15)
plt.text(0.1, 3, 'y = -log(x)', fontsize=15)
plt.xlim(-0.3, 1.4)
plt.ylim(-0.5, 4)
plt.scatter(0.5, -np.log(0.5))
plt.show()

# 극한
# 극한에 대해서는 어떠한 식을 코드로 표현할 수 있다 정도로만 이해하며 참고
# 극한에서 알아야 할 사실은 x가 어떤 값 a에 가까이 다가갈 때, a에 '한없이 가까이 간다' 일뿐, a에 도달하지 않는다는 점.
# 이를 표현할 때, 엡실론(epsilon)이라는 아주 작은 값(ex, 0.0001)등으로 표현

from sympy import *
init_printing()

x, y, z = symbols('x y z')
a, b, c, t = symbols('a, b, c, t')

## lim(x-> 1): ((x**3- 1)/ (x-1))= 3
print("극한값: ", limit((x**3- 1)/ (x- 1), x, 1))
plot(((x**3- 1)/ (x- 1)), xlim=(-5, 5), ylim=(-1, 10))

# lim(x-> oo): (1+ x)/ x
print("극한값: ", limit((x+ 1)/ x, x, oo))
plot((x+ 1)/ x, xlim=(-10, 10), ylim=(-5, 5))

# lim(x-> 1): (sqrt(x+ 3)- 2)/ (x- 1) = 1/ 4
print("극한값: ", limit((sqrt(x+ 3)- 2)/ (x- 1), x, 1))
plot((sqrt(x+ 3)- 2)/ (x- 1), xlim=(-5, 12), ylim=(-0.5, 1))

# 삼각함수의 극한

# lim(x-> (pi/ 2)+ 0): tan(x) = -oo
# lim(x-> (pi/ 2)- 0): tan(x) = oo
print("극한값: ", limit(tan(x), x, pi/ 2, '+'))
print("극한값: ", limit(tan(x), x, pi/ 2, "-"))
plot(tan(x), xlim=(-3.14, 3.14), ylim=(-6, 6))

# lim(x-> 0): sin(x)/ x = 1
print("극한값: ", limit(sin(x)/ x, x, 0))
plot(sin(x)/ x, ylim=(-2, 2))

# lim(x-> 0): x* sin(1/ x)
print("극한값: ", limit(x* sin(1/ x), x, 0))
plot(x* sin(1/ x), xlim=(-2, 2), ylin=(-1, 1.5))


#40m 53s