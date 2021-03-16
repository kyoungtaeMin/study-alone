# 선형 모델 (Linear Models)
# - 선형 모델은 과거부터 지금까지 널리 사용되고 연구되고 있는 기계학습 방법
# - 선형 모델은 입력 데이터에 대한 선형 함수를 만들어 예측 수행
# - 회귀 분석을 위한 선형 모델은 다음과 같이 정의

#   y^(w, x) = w0 + w1x1 + ... + wpxp

# x : 입력 데이터
# w : 모델이 학습할 파라미터
# w0 : 편향
# w1~wp : 가중치

# 선형 회귀 (Linear Regression)
# - 선형 회귀(Linear Regression)또는 최소제곱볍(Ordinary Least Squares)은 가장 간단한 회귀 분석을 위한 선형 모델
# - 선형 회귀는 모델의 예측과 정답 사이의 평균제곱오차(Mean Squared Error)를 최소화하는 학습 파라미터 w를 찾음
# - 평균제곱오차는 아래와 같이 정의

#   MSE = 1/N * sigma(i=1->N)(y1 - y^i)**2

# y : 정답
# y^ : 예측 값을 의미 (Linear Models에서 나온 예측 값)

# - 선형 회귀 모델에서 사용하는 다양한 오류 측정 방법
#   - MAE (Mean Absolute Error)
#   - MAPE (Mean Absolute Percentage Error)
#   - MSE (Mean Squared Error)
#   - MPE (Mean Precentage Error)


import numpy as np
import matplotlib.pyplot as plt
plt.style.use(['seaborn-whitegrid'])
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

noise = np.random.rand(100, 1)
X = sorted(10 * np.random.rand(100, 1)) + noise
y = sorted(10 * np.random.rand(100))

plt.scatter(X, y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LinearRegression()
model.fit(X_train, y_train)

print("선형 회귀 가중치: {}".format(model.coef_))
print("선형 회귀 편향: {}".format(model.intercept_))
print("학습 데이터 점수: {}".format(model.score(X_train, y_train)))
print("평가 데이터 점수: {}".format(model.score(X_test, y_test)))

predict = model.predict(X_test)

plt.scatter(X_test, y_test)
plt.plot(X_test, predict, '--r')

# 머신러닝을 수행할 때, 항상 데이터를 먼저 잘 이해해야한다.
# 데이터를 큰 그림으로 관찰, 분석, 시각화를 통해 어떤식으로 머신러닝을 수행해야 할지 고민을 하고 수행해야한다.

# 보스턴 주택 가격 데이터 활용
# - 주택 가격 데이터는 도시에 대한 분석과 부동산, 경제적인 정보 분석 등 많은 활용 가능한 측면들이 존재
# - 보스턴 주택 가격 데이터는 카네기 멜론 대학교에서 관리하는 StatLib 라이브러리에서 가져온 것
# - 헤리슨(Harrison, D)과 루빈펠트(Rubinfeld, D.L)의 논문 "Hedonic prices and the demeand for clean air', J.Environ.Economics & Management"에서 보스턴 데이터가 사용
# - 1970년도 인구 조사에서 보스턴의 506개 조사 구역과 주택 가격에 영향을 주는 속성 21개로 구성
from sklearn.datasets import load_boston

boston = load_boston()
print(boston.keys())
print(boston.DESCR)

import pandas as pd

boston_df = pd.DataFrame(boston.data, columns=boston.feature_names)
boston_df['MEDV'] = boston.target
boston_df.head(5)
boston_df.describe()

for i, col in enumerate(boston_df.columns):
    plt.figure(figsize=(8, 4))
    plt.plot(boston_df[col])
    plt.title(col)
    plt.xlabel('Town')
    plt.tight_layout()

for i, col in enumerate(boston_df.columns):
    plt.figure(figsize=(8, 4))
    plt.scatter(boston_df[col], boston_df['MEDV'])
    plt.title(col)
    plt.xlabel(col, size=12)
    plt.ylabel('MEDV', size=12)
    plt.tight_layout()

import seaborn as sns

sns.pairplot(boston_df)

# 보스턴 주택 가격에 대한 선형 회귀
from sklearn.linear_model import LinearRegression

model = LinearRegression(normalize=True)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2)
model.fit(X_train, y_train)
print("학습 데이터 점수: {}".format(model.score(X_train, y_train)))
print("평가 데이터 점수: {}".format(model.score(X_test, y_test)))

# 데이터를 두개로 분리하고 모델을 생성 및 검증하였지만, 데이터를 분리하였기 때문에 훈련에 사용할 수 있는 양도 작아지고, 분리가 잘 안된 경우에는 잘못된 검증이 될 수 있음
# 이럴 경우에는 테스트셋을 여러개로 구성하여 교차 검증을 진행
# cross_val_score() 함수는 교차 검증을 수행하여 모델을 검증
# 다음 예제는 모델 오류를 측정하는 점수로 NMSE(Negative Mean Squared Error)를 사용
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, boston.data, boston.target, cv=10, scoring='neg_mean_squared_error')
print("MNSE scores: {}".format(scores))
print("MNSE scores mean: {}".format(scores.mean()))
print("MNSE scores std: {}".format(scores.std()))

# 회귀모델의 검증을 위한 또 다른 측정 지표 중 하나로 결정 계수(coefficient of determination, R**2)사용
r2_scores = cross_val_score(model, boston.data, boston.target, cv=10, scoring='r2')

print("R2 scores: {}".format(r2_scores))
print("R2 scores mean: {}".format(r2_scores.mean()))
print("R2 scores std: {}".format(r2_scores.std()))

# 생성된 회귀 모델에 대해서 평가를 위해 LinearRegression 객체에 포함된 두 개의 속성 값을 통해 수식을 표현
#   - inercept_ : 추정된 상수항
#   - coef_ : 추정된 가중치 벡터
print('y = '+ str(model.intercept_)+ " ")
for i, c in enumerate(model.coef_):
    print(str(c)+ " * x"+ str(i))

from sklearn.metrics import mean_squared_error, r2_score

y_train_predict = model.predict(X_train)
rmse = (np.sqrt(mean_squared_error(y_train, y_train_predict)))
r2 = r2_score(y_train, y_train_predict)

print("RMSE: {}".format(rmse))
print("R2 score: {}".format(r2))

y_test_predict = model.predict(X_test)
rmse = (np.sqrt(mean_squared_error(y_test, y_test_predict)))
r2 = r2_score(y_test, y_test_predict)

print("RMSE: {}".format(rmse))
print("R2 score: {}".format(r2))

def plot_boston_prices(expected, predicted):
    plt.figure(figsize=(8, 4))
    plt.scatter(expected, predicted)
    plt.plot([5, 50], [5, 50], '--r')
    plt.xlabel('True price ($1.000s)')
    plt.ylabel('Predicted price ($1,000s)')
    plt.tight_layout()

predicted = model.predict(X_test)
expected = (y_test)

plot_boston_prices(expected, predicted)
