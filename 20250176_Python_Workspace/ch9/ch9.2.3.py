## 클래스(Class)

# 9.2.3. 메서드(method)
# : 클래스 안에 정의한 함수
# : 메서드는 클래스 안에 여러 개 만들 수 있음
# : 메서드의 첫 번째 전달값으로 항상 self를 넣어야 함 (self : 객체인 자기자신을 의미)

# 공격할 수 있는 유닛만을 위한 클래스 정의
class AttackUnit:
    # 생성자 정의의
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
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

# 화염방사병 : 공격 유닛, 화염방사기를 사용함
flamethrower1 = AttackUnit("화염방사병", 50, 16) # 객체 생성, 체력 50, 공격력 16, 진동형, 파이어뱃
flamethrower1.attack("5시") # 5시 방향으로 공격 명령

# 25만큼의 공격을 2번 받음
flamethrower1.damaged(25) # 남은 체력 25
flamethrower1.damaged(25) # 남은 체력 0