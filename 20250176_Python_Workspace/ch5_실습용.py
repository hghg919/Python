## 자료구조

##################################################
# 5.1. 리스트(List)

# 유사한 특성을 가지는 대상이 비슷한 행동을 한다면?
# - 10명이 각각 차를 몰고 서울역에서 사당역으로 이동
# - 10명이 함께 지하철을 타고 이동

# 유사한 특성을 가지는 변수가 여러개 필요하다면?
# - 학생 10명의 점수를 저장
#  >> score0 = 87; score1 = 84, score2 = 95, ... score9 = 63
# - 학생이 3000명이라면?
# - 개별적인 변수의 생성과 값의 할당으로 많은 변수 이름이 필요
#  ==> 변수의 합과 평균 등 연산을 할 경우 코딩이 복잡하고 번거로움

# 5.1.1. 리스트 생성하기

# 지하철 칸별로 10명, 20명, 30명 승차
subway1 = 10
subway2 = 20
subway3 = 30
print(subway1, subway2, subway3)

# 지하철 칸이 수십칸이라면? ==> 칸의 개수에 대응되는 변수 이름을 만들고 값을 할당

# 리스트를 사용하면 변수 하나로 관리 가능!
# (형식) 리스트명 = [값1, 값2, ...]
subway = [10, 20, 30]
print(subway)

# 리스트의 특징
# - 여러 값을 가질 수 있다.
# - 각 값의 자료형은 다를 수 있다.
# - 값의 중복을 허용하며 순서를 보장한다.

# 빈 리스트 생성하기
empty_list = []
empty_list2 = list()
print(empty_list, empty_list2)

# 5.1.2. 값 추가/삽입/삭제하기

# 1) 리스트에 저장된 값의 위치 확인
# (형식) 리스트.index(위치를 찾을 값)
# - 리스트의 값에는 인덱스(index)로 접근
subway = ["푸", "피글렛", "티거"]
print(subway)

# 피글렛이 몇 번째 칸에 탔는가? (인덱스는 항상 0부터 시작!)
print(subway.index("피글렛"))
# 지하철에 타지 않은 뽀로로를 찾고 싶어 index() 함수를 쓰면 에러 발생
# print(subway.index("뽀로로"))

# 2) 리스트에 값을 추가
# (형식) 리스트.append(추가할 값)
# - 리스트의 맨 뒤에 값을 추가

# 이요르 탑승
subway.append("이요르")
print(subway)

# 3) 리스트에 값을 삽입
# (형식) 리스트.insert(인덱스, 삽입할 값)
# - 리스트의 어떤 위치든 값을 넣을 수 있음
# - 삽입한 값의 뒤에 있는 값의 위치는? ==> 1씩 뒤로 밀림

# 루를 푸와 피글렛 사이(인덱스 1 위치)에 삽입
subway.insert(1, "루")
print(subway)

# 4) 리스트에서 값을 반환 후 삭제
# (형식) 반환된 값 = 리스트.pop()
# - 리스트의 가장 마지막 위치에 있는 값을 꺼냄

# 지하철 역마다 한 명씩 내림
print(subway.pop()) # 이요르 내림
print(subway)

print(subway.pop()) # 티거 내림
print(subway)

print(subway.pop()) # 피글렛 내림
print(subway)

# 5) 리스트의 모든 값 삭제
# (형식) 리스트.clear()
# - 리스트 안에 있는 모든 값을 지우고 빈 리스트로 만듦

# 지하철에서 모두 내림
subway.clear()
print(subway)

# 5.1.3. 중복 값 확인하기
# (형식) 리스트.count(찾을 값)
# - 리스트 안에 같은 값이 몇 개인지 확인

# 같은 이름이 몇 명 있는지 확인
subway = ["푸", "피글렛", "티거"]
subway.append("푸") # 푸 추가가
print(subway)
print(subway.count("푸")) # subwayt 안에 "푸"가 몇 개 있는지 확인

# 5.1.4. 리스트 정렬하기
num_list = [5, 2, 4, 3, 1]

# (형식) 리스트.sort()
num_list.sort() # 오른차순 정렬
print(num_list)

# (형식) 리스트.sort(reverse=True)
num_list.sort(reverse=True) # 내림차순 정렬
print(num_list)

# (형식) 리스트.reverse()
# - reverse() 함수는 정렬과는 전혀 상관없음
# - 단순히 리스트 안에 있는 값을 순서를 뒤집는 역활만 함
num_list.reverse() # 순서 뒤집기
print(num_list)

# (형식) 새로운 리스트 = sorted(리스트)
# - 원본 리스트 변경 없이 정렬된 리스트를 새로 생성
my_list = [1, 3, 2]
my_list.sort() # 리스트 정렬
print(my_list) # my_list 리스트 데이터 변경

your_list = [1, 3, 2]
new_list = sorted(your_list) # 정렬할 리스트는 소괄호 안에 넣음
print(your_list) # your_list 리스트 데이터는 변경되지 않음
print(new_list) # 정렬된 새로운 리스트 

# 5.1.5. 리스트 확장하기
# - 리스트에는 서로 다른 자료형의 값을 넣을 수 있음
#   . 정수형, 실수형, 문자열, 불형, 리스트형, ...
mix_list = ["푸", 20, True, [5, 2, 4, 3, 1]]
print(mix_list)

# (형식) 리스트1.extend(리스트2)
# - 리스트1 뒤에 리스트2를 합침
mix_list = ["푸", 20, True]
num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_list) # 리스트 합치기
print(mix_list)
print(num_list)

#############################################################
# 5.2. 딕셔너리(Dictionary)

# - 리모컨 키와 차의 관계 ==> 리모컨 키를 눌렀더니 주변의 여러차가 동시에 열린다면?
# - 영어사전에 있는 영어 단어와 뜻의 관계

# 딕셔너리 : key와 value 한 쌍으로 이루어진 값들을 담기 위한 자료구조
# (형식) 딕셔너리명 = {key1: value1, key2: value2, ...}
# - key는 중복을 허용하지 않으며 변하지 않는 값을 사용해야 함
# - 파이썬 3.7 버전부터 순서를 보장

# 5.2.1. 딕셔너리 생성하기
cabinet = {3: "푸", 100: "피글렛"}

# 빈 딕셔너리 생성
empty_dict = {} # 빈 딕셔너리 생성하기
empty_dict2 = dict()
print(empty_dict, empty_dict2)

# key를 이용하여 딕셔너리 값(value)에 접근
# - 딕셔너리명에 대괄호를 붙이고 그 안에 key를 넣으면 key에 해당하는 value에 접근
print(cabinet[3]) # key 3에 해당하는 value ==> "푸"
print(cabinet[100]) # key 100에 해당하는 value ==> "피글렛"

# 대괄호 대신 get() 함수를 사용하여 값에 접근 가능
# (형식) 딕셔너리.get(key)
print(cabinet.get(3))

# 대괄호와 get() 사용의 차이점 : 정의되는 않은 key를 이용하여 value를 찾을 때 발생
# - 대괄호 이용 : 에러 발생(KeyError)
# - get() 함수 이용 : 오류 없이 None 출력
print(cabinet.get(5)) # None 출력
print("hi")
# print(cabinet[5])
# print("hi")

print(cabinet.get(5, "사용 가능")) # key에 해당하는 값이 없으면 기본값을 사용하게 함.

# key가 딕셔너리에 있는 확인
# (형식) key in 딕셔너리
# - 해당 key가 있을 때 True, 없을 때 False를 반환
print(3 in cabinet)
print(5 in cabinet)

# key는 정수형뿐만 아니라 문자열도 가능
cabinet = {"A-3": "푸", "B-100": "피글렛"}
print(cabinet["A-3"])
print(cabinet["B-100"])
print(cabinet.get("B-100"))

# 문자열에 대한 in 연산
# - 부분 문자열 포함 여부 확인
print("곰" in "곰돌이") # True
print("돌이" in "곰돌이") # True
print("푸" in "곰돌이") # False

# 5.2.2. 값 변경/추가/삭제하기
# 딕셔너리의 값에는 key를 통해 접근할 수 있음
# - key에 해당하는 value로 딕셔너리에 접근했을 때
#   . key에 해당하는 값이 있으면 key를 유지하면서 기존 value를 새로운 value로 변경
#   . key에 해당하는 값이 없으면 key와 value 한 쌍으로 된 값을 딕셔너리에 새로 추가
cabinet = {"A-3": "푸", "B-100": "피글렛"}
print(cabinet)
cabinet["A-3"] = "티거" # key에 해당하는 값이 있을 때 -> 값 변경
cabinet["C-20"] = "이요르" # key에 해당하는 값이 없을 때 -> 값 추가
print(cabinet)

# 딕셔너리 값 삭제
# (형식) del 딕셔너리[key]
# - key에 해당하는 값을 찾아서 삭제
del cabinet["A-3"] # key "A-3"에 해당하는 값 삭제
print(cabinet)

# 5.2.3. 값 확인하기

# 딕셔너리.keys() : 딕셔너리에 있는 key 확인
print(cabinet.keys()) # key만 출력

# 딕셔너리.values() : 딕셔너리에 있는 value 확인
print(cabinet.values()) # value만 출력

# 딕셔너리.items() : key와 value 둘 다 확인
print(cabinet.items()) # key, value 한 쌍으로 출력

# 딕셔너리.clear() : 딕셔너리에 있는 모든 값을 삭제
cabinet.clear() # 값 전체 삭제
print(cabinet)

##################################################
# 5.3. 튜플(Tuple)

# - 리스트의 읽기 전용 버전
#   . 처음 정의할 때를 제외하고 값의 변경이나 추가, 삭제 등이 불가
#   . 값의 중복을 허용
#   . 순서를 보장
#   . 리스트보다 속도가 빠름
# (형식) 튜플명 = (값1, 값2, ...)

# 빈 튜플 생성

# 튜플의 값의 접근 : 인덱스를 이용

# 튜플을 이용하면 변수들의 값을 손쉽게 변경 가능능


##################################################
# 5.4. 세트(Set)

# - 집합을 표현하기 위한 자료구조
#   . 값의 중복을 허용하지 않음
#   . 순서를 보장하지 않음
# (형식) 세트명 = {값1, 값2, ...}

# 같은 값을 여러 번 넣어도 하나만 저장

# 세트 변수 선언

# 빈 세트 생성

# 교집합
# - 두 집합에서 공통 값을 뽑아내는 기능
# - & 기호나 intersection() 함수 이용
# (자바와 파이썬을 모두 다룰 수 있는 개발자)

# 합집합
# - 두 집합을 합치는 기능
# - | (파이프, pipe) 기호나 union() 함수 사용
# (자바 또는 파이썬을 다룰 수 있는 개발자)

# 차집합
# - 한 집합에서 다른 집합을 제외하는 기능
# - - (마이너스) 기호 또는 difference() 함수 사용
# (자바는 할 수 있지만 파이썬은 할 줄 모르는 개발자)

# add() 함수
# - 집합에 값을 추가할 때 사용
# 파이썬 개발자 추가 (기존 개발자: 푸, 이요르)

# remove() 함수
# - 집합에서 값을 제외할 때 사용
# 자바 개발자 삭제(기존 개발자: 푸, 피글렛, 티거)


##################################################
# 5.5. 자료구조 변환하기

# - 필요에 따라 다른 자료구조로 변환
# - 변환 방법 : 바꾸고 싶은 자료구조를 나타내는 명령어의 소괄호 안에 바꿀 자료구조명을 넣음
