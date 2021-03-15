# import travel.thailand
# # travel 뒤에 오는 자리는 모듈이나 패키지만 올 수 있다.

# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# # from 절에서는 class를 import 할 수 있다.

# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# import random
# import inspect
# from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# print(inspect.getfile(random))
# print(inspect.getfile(thailand))
