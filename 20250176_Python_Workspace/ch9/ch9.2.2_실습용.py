## 클래스(Class)

# 9.2.2. 인스턴스 변수
# : 메서드 안에 정의한 변수로 self와 함께 사용

## 메서드 내부에서의 사용법 : self.변수명
class Unit:
    def __init__(self, name, hp, damage): # 생성자, self 외 전달값 3개
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛을 생성했습니다.".format(self.name))
        print("체력 {}, 공격력 {}".format(self.hp, self.damage))

# 전투기: 공중 유닛, 은폐 불가
stealth1 = Unit("전투기", 80 , 5)
# 인스턴스 변수 접근
print("유닛 이름 : {}, 공격력 : {}".format(stealth1.name, stealth1.damage))

## 클래스 외부에서의 인스턴스 변수 정의할 때 : 객체명.변수명 = 값
## - 특정 객체만을 위한 인스턴스 변수가 필요한 경우에 클래스 외부에서 별도로 정의 가능
## - 해당 객체를 제외한 다른 객체들은 새로 정의한 인스턴스 변수를 사용하지 못함

# 은폐 가능한 stealth2 전투기를 위한 객체 생성
# - 은폐 정보를 관리하기 위한 cloaking 인스턴스 변수를 클래스 외부에서 정의
# 은폐 가능
stealth2 = Unit("업그레이드한 전투기", 80 ,5)
# 업그레이드한 전투기만을 위한 특별한 인스턴스 변수 정의, 은폐 상태
stealth2.cloaking = True

if stealth2.cloaking == True:
    print("{}는 현재 은폐 상태입니다.".format(stealth2.name))

# 오류 발생
#if stealth1.cloaking == True:
#    print("{}는 현재 은폐 상태입니다.".format(stealth1.name))

