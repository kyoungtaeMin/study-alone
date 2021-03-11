class Unit():
    def __init__(self):
        print('Unit 생성자')

class Flyable():
    def __init__(self):
        print('Flyable 생성자')

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

# 상속 받을 때 사용.
# () 를 써줘야함, self 를 기재할 필요없음.
# super 를 활용하여 다중상속을 받을 때는, 마지막에 상속받는 class에
# 대해서만 호출이 된다. 따라서 각각 정의를 해줘야 한다.

dropship = FlyableUnit()
