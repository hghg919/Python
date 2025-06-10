## 클래스(Class)

##################################################
# 9.1. 게임 소개
# - 세 종족 사이의 전쟁
# - 유닛(unit)을 최대한 빠르게 많이 만들어서 적을 궤멸시키는 것이 목표

# 게임에서 만들 유닛
# - 보병(마린): 공격 유닛, 군인, 총을 쏠 수 있음
# - 탱크(시즈탱크): 공격 유닛, 포를 쏠 수 있음, 두 가지 모드(일반/시즈 모드)
# - 전투기(레이스): 공중 유닛, 은폐 기능
# - 화염방사병(파이어뱃): 공격 유닛, 화염방사기 사용
# - 요격기(발키리): 공중 공격 유닛, 미사일 여러 발을 한 번에 발사
# - 호버 바이크(벌쳐 -75-): 지상 유닛, 기동성 좋음
# - 우주 순양함(배틀크루져): 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
# - 보급고(서플라이 디팟): 건물 유닛, 1개 건물 유닛 = 8유닛


# 보병: 공격 유닛, 군인, 총을 쏠 수 있음
name = "보병" # 이름
hp = 40 # 체력
damage = 5 # 공격력

print("{} 유닛을 생성했습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크: 공격 유닛, 포를 쏠 수 있음, 두 가지 모드(일반/시 모드)
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{} 유닛을 생성했습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# 새로 탱크2 추가
tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35
 
print("{} 유닛을 생성했습니다.".format(tank2_name))
print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

# 공격 함수
def attack(name, location, damage):
    print("{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)
