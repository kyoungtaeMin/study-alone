# scikit-learn 특징
#   - 다양한 머신러닝 알고리즘을 구현한 파이썬 라이브러리
#   - 심플하고 일관성 있는 API, 유용한 온라인 문서, 풍부한 예제
#   - 머신러닝을 위한 쉽고 효율적인 개발 라이브러리 제공
#   - 다양한 머신러닝 관련 알고리즘과 개발을 위한 프레임워크와 API 제공
#   - 많은 사람들이 사용하며 다양한 환경에서 검증된 라이브러리

# scikit-learn 주요 모듈
#   - sklearn.preprocessing : 다양한 데이터 전처리 기능 제공(변환, 정규화, 스케일링 등)
#   - sklearn.model_selection : 교차 검증을 위해 데이터를 학습/테스트용으로 분리, 최적 파라미터를 추출하는 API 제공(GridSearch 등)
#   - sklearn.metrics : 분류, 회귀, 클러스터링, Pairwise에 대한 다양한 성능 측정 방법 제공(Accuracy, Precision, Recall, ROC-AUC, RMSE 등)
#   - sklearn.pipeline : 특징 처리 등의 변환과 ML 알고리즘 학습, 예측 등을 묶어서 실행할 수 있는 유틸리티 제공
#   - sklearn.ensemble : 앙상블 알고리즘 제공(Random Forest, AdaBoost, GradientBoost 등)

# estimator API
#   - 일관성 : 모든 객체는 일관된 문서를 갖춘 제한된 메서드 집합에서 비롯된 공통 인터페이스 공유
#   - 검사(inspection) : 모든 지정된 파라미터 값은 공개 속성으로 노출
#   - 제한된 객체 계층 구조
#     - 알고리즘만 파이썬 클래스에 의해 표현
#     - 데이터 세트는 표준 포맷(NumPy 배열, Pasdas DataFrame, Scipy 희소 행렬)으로 표현
#     - 매개변수명은 표준 파이썬 문자열 사용
#   - 구성 : 많은 머신러닝 작업은 기본 알고리즘의 시퀀스로 나타낼 수 있으며, Scikit-Learn은 가능한 곳이라면 어디서든 이 방식을 사용
#   - 합리적인 기본값 : 모델이 사용자 지정 파라미터를 필요로 할 때 라이브러리가 적절한 기본값을 정의

# API 사용 방법
#   - Scikit-Learn으로 부터 적절한 estimator 클래스를 임포트해서 모델의 클래스 선택
#   - 클래스를 원하는 값으로 인스턴스화해서 모델의 하이퍼파라미터 선택
#   - 데이터를 특징 배열과 대상 벡터로 배치
#   - 모델 인스턴스의 fit() 메서드를 호출해 모델을 데이터에 적합
#   - 모델을 새 데이터에 대해서 적용
#     - 지도 학습 : 대체로 predict() 메서드를 사용해 알려지지 않은 데이터에 대한 레이블 예측
#     - 비지도 학습 : 대체로 transform() 이나, predict() 메서드를 사용해 데이터의 속성을 변환하거나 추론
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
plt.style.use(['seaborn-whitegrid'])

x = 10 * np.random.rand(50)
y = 2 * x + np.random.rand(50)
plt.scatter(x, y)
# 적절한 estimator 클래스를 임포트해서 모델의 클래스 선택
# 클래스를 원하는 값으로 인스턴스화해서 모델의 하이퍼파라미터 선택
model = LinearRegression(fit_intercept=True)
model
