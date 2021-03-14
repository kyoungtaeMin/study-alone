from random import *

class Unit: # AttackUnit 의 부모 class
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print('{0} 유닛이 생성되었습니다.'.format(name))
    
    def move(self, location):
        print('{0} : {1} 방향으로 이동합니다. [속도 : {2}]'\
            .format(self.name, location, self.speed))
    
    def damaged(self, damage):
        print('{0} : {1}의 데미지를 입었습니다.'.format(self.name, damage))
        self.hp -= damage
        print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
        if self.hp <= 0:
            print('{0} : 파괴되었습니다.'.format(self.name))

# __init__
# 파이썬에서 쓰이는 생성자.
# 객체가 만들어질 때, 자동으로 호출되는 부분.

# self 를 제외한 변수를 모두 입력해 주어야 작동

# 멤버 변수
# self.--- ---부분. class 내에서 정의된 변수를 가리킴

class AttackUnit(Unit): # Unit 의 자식 class, FlyableAttackUnit 의 부모 class
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed) # 상속
        self.damage = damage

    def attack(self, location):
        print('{0} : {1} 방향으로 적군 공격. [공격력 {2}]'\
            .format(self.name, location, self.damage))

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, '마린', 40, 1, 5)
    
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print('{0} : 스팀팩을 사용합니다. (HP 10 감소)'.format(self.name))
        else:
            print('{0} : 체력이 부족합니다.'.format(self.name))

class Tank(AttackUnit):
    seize_developed = False 

    def __init__(self):
        AttackUnit.__init__(self, '탱크', 150, 1, 35)
        self.seize_mode = False
    
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        if self.seize_mode == False:
            print('{0} : 시즈모드 전환.'.format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print('{0} : 시즈모드 해제.'.format(self.name))
            self.damage /= 2
            self.seize_mode = False

class Flyable: # FlyableAttackUnit 의 부모 class
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print('{0} : {1} 방향으로 날아갑니다. [속도 : {2}]'\
            .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable): # AttackUnit , Flyable 의 자식 class
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed = 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, '레이스', 80, 20, 10)
        self.clocked = False
    
    def clocking(self):
        if self.clocked == True:
            print('{0} : 클로킹 모드 해제'.format(self.name))
            self.clocked == False
        else:
            print('{0} : 클로킹 모드 전환'.format(self.name))
            self.clocked == True


# Unit

marine1 = Unit('마린', 40, 5) # class 로 인해 만들어지는 객체 = Unit class 의 instance
marine2 = Unit('마린', 40, 5)

# AttackUnit

vulture = AttackUnit('벌쳐', 50, 5, 15)
vulture.move('5시')

vulture.damaged(25)
vulture.damaged(25)

# FlyableAttackUnit

wraith = FlyableAttackUnit('빼앗은 레이스', 80, 15, 10)
wraith.clocking = True

if wraith.clocking == True:
    print('{0} 는 현재 클로킹 상태입니다.'.format(wraith.name))

# wraith2 를 제외한 다음 객체에서는 clocking 함수가 정의되지 않았으므로 쓸 수 없음.

valkyrie = FlyableAttackUnit('발키리', 200, 10, 10)
valkyrie.fly(valkyrie.name, '3시')

battlecruiser = FlyableAttackUnit('배틀크루저', 500, 50, 3)
battlecruiser.fly(battlecruiser.name, '9시')
battlecruiser.move('9시')

supply_depot = BuildingUnit('서플라이 디폿', 500, '7시')

def game_start():
    print('[알림] 새로운 게임을 시작합니다.')

def game_over():
    # pass
    print('Player : GG')
    print('[Player] 님이 게임에서 퇴장하셨습니다.')

print('='*50)

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
    unit.move('1시')

Tank.seize_developed = True
print('[알림] 탱크 시즈 모드 개발이 완료되었습니다.')

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

for unit in attack_units:
    unit.attack('1시')

for unit in attack_units:
    unit.damaged(randint(5, 21))

game_over()



class House():
    def __init__(self, location, house_type, deal_type, price,\
        completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price,\
            self.completion_year)

houses = []
house1 = House('대전 신탄진', '아파트', '매매', '4억', '2018년')
house2 = House('대전 둔산동', '빌라', '전세', '1억 5천', '2017년')
house3 = House('대전 관평동', '원룸', '월세', '500/30', '2020년')
houses.append(house1)
houses.append(house2)
houses.append(house3)

print('='*50)
print('총 {0}대의 매물이 있습니다.'.format(len(houses)))
for house in houses:
    house.show_detail()
