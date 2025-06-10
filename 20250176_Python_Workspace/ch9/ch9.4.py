##################################################
# 9.4. 동작 없이 일단 넘어가기: pass

# : 세부 동작을 정의하지 않은 채로 두고 일단은 그냥 넘어갈 때 사용
# : 보통 완성되지 않은 if 문, for 문, while 문, 클래스, 메서드 등에서 사용하고 나중에 세부 동작을 정의

class Unit:
    def __init__(self, name, hp, speed): # speed 추가
        self.name = name
        self.hp = hp
        self.speed = speed # 지상 이동 속도

    def move(self, location): # 이동 동작 정의
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]" \
            .format(self.name, location, self.speed))

# 건물 유닛
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

# 보급고: 건물 유닛, 1개 건물 유닛 = 8유닛
supply_depot = BuildingUnit("보급고", 500, "7시") # 체력 500, 생성 위치 7시

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()
