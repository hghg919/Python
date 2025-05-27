## 클래스(Class)

# 9.2.1. 생성자(constructor): __init__()
# : 객체를 생성할 때 따로 호출하지 않아도 자동으로 호출되는 메서드
class Unit:
    def __init__(self, name, hp, damage): # 생성자, self 외 전달값 3개
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛을 생성했습니다.".format(self.name))
        print("체력 {}, 공격력 {}".format(self.hp, self.damage))


# 객체를 생성할 때 self를 제외하고 __init__() 생성자에 정의한 개수만큼 전달값을 넘겨줘야 함
soldier1 = Unit("보병", 40, 5)
soldier2 = Unit("보병", 40, 5)
tank = Unit("탱크", 150, 35)
#soldier3 = Unit("보병")
#soldier3 = Unit("보병", 40)


# 생성자를 정의하지 않았다면 클래스명만으로 객체를 생성
# (형식) 변수명 = 클래스명()

class TestUnit:
    def __init__(self):
        self.name = "홍길동"
        print("제 이름은 {}입니다.".format(self.name))

person1 = TestUnit()