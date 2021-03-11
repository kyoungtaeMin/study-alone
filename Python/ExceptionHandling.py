try:

    print("나누기 전용 계산기")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    #nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)
# 예외처리로 에러 메세지를 지정할 수 있다. 하지만
#  err을 사용하면 에러 내용을 출력시킨다.
