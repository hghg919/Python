## 클래스(Class)

##################################################
# 9.3. 클래스 상속하기

# 9.3.1. 상속이란?
# : 클래스에서 공통 부분은 그대로 사용하고
# : 확장이 필요한 부분만 추가로 구현하고자 할 때 상속(inheritance)을 구현

# - 부모 클래스 : 공통 부분이 구현된 클래스
# - 자식 클래스 : 부모 클래스를 상속하는 클래스
# (형식) class 자식 클래스(부모 클래스):

# 공격을 할 수 없는 유닛을 구현하려면? (AttackUnit 클래스로 객체를 생성할 수 없음)
# : Unit 클래스를 일반적인 유닛을 위한 클래스로 수정
# : AttackUnit 클래스는 유닛의 공통 요소(name, hp)를 상속 받아서 사용

class Unit:
    def __init__(self, name, hp):
        self.name = name # 모든 Unit들의 공통 속성 (이름)
        self.hp = hp     # 모든 Unit들의 공통 속성 (체력)

class AttackUnit(Unit): # Unit 클래스 상속
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # 부모 클래스의 생성자 호출
        self.damage = damage
    
    def attack(self, location): # 전달받은 방향으로 공격
        print("{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage)) # 공간이 좁아서 2줄로 나눔

    def damaged(self, damage): # damage만큼 유닛 피해
        # 피해 정보 출력
        print("{0} : {1}만큼 피해를 입었습니다.".format(self.name, damage))
        self.hp -= damage # 유닛의 체력에서 전달받은 damage만큼 감소
        # 남은 체력 출력
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0: # 남은 체력이 0 이하이면
            print("{0} : 파괴됐습니다.".format(self.name)) # 유닛 파괴 처리

flamethrower1 = AttackUnit("화염방사병", 50, 16)
flamethrower1.attack("5시") # 5시 방향으로 공격 명령

# 25만큼의 공격을 2번 받음
flamethrower1.damaged(25) # 남은 체력 25
flamethrower1.damaged(25) # 남은 체력 0

## 서로 관련있는 클래스들에서 공통 부분을 모아 부모 클래스로 정의하고, 자식 클래스에서는 필요한 부분을 확장해 사용하면?
## - 불필요한 코드의 중복 작성을 방지
## - 수정이나 추가 사항이 생길 때 작업 범위롤 최소화할 수 있음