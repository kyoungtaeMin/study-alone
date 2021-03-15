# ----- 내장 함수는 python 자체에서 제공해줘서 바로 사용할 수 있는 것들.
# list of built in functions 로 검색 ----

# input : 사용자 입력을 받는 함수

# language = input("어느 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시

# print(dir())
# import random
# print(dir())
# import pickle
# print(dir(random))

# list = [1, 2, 3]
# print(dir(list))


# ----- 외장 함수는 외부에서 직접 우리가 import 해서 사용하는 것들.
# list of python module 이라고 검색해서 알하서 필요한거 찾아서 쓰도록하자

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir과 같은 기능)
# import glob
# print(glob.glob("*.py"))  # 확장자가 .py인 모든 파일에 대해서 알려줌

# os : 운영체제에서 제공하는 기본
# import os
# print(os.getcwd())  # 현재 디렉토리

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print("폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)  # 폴더를 생성하는 함수
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir()) # 폴더 / 파일 목록 조회

# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
# today = datetime.date.today()  # 오늘 날짜 저장
# td = datetime.timedelta(days=100)
# print("우리가 만난지 100일은 ", today + td)  # 오늘 부터 100일 후
