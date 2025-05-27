## 클래스(Class)

# 9.2.3. 메서드(method)
# : 클래스 안에 정의한 함수
# : 메서드는 클래스 안에 여러 개 만들 수 있음
# : 메서드의 첫 번째 전달값으로 항상 self를 넣어야 함 (self : 객체인 자기자신을 의미)

# 공격할 수 있는 유닛만을 위한 클래스 정의
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage


# 화염방사병: 공격 유닛, 화염방사기를 사용함

# 25만큼의 공격을 2번 받음
